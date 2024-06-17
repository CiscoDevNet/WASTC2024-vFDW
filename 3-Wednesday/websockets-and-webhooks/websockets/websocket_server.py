import asyncio
import websockets
import json

connected_clients = set()
admin_clients = set()  # Separate set for admin clients
total_messages = 0
message_history = []  # Store message history


async def echo(websocket, path):
    global total_messages
    if path == "/admin":
        # Handle the admin connection in a separate coroutine
        await admin_handler(websocket, path)
        return

    # Assign a unique name or identifier to the client
    client_name = f"Client_{websocket.remote_address[1]}"
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message from {client_name}: {message}")
            await websocket.send(f"Echo: {message}")
            total_messages += 1
            message_data = (client_name, message)
            message_history.append(message_data)  # Add to message history
            await update_admin_clients()  # Update stats
            await send_message_update_to_admins(
                message_data
            )  # Send new message to admins
    finally:
        connected_clients.remove(websocket)
        await update_admin_clients()  # Update stats


async def admin_handler(websocket, path):
    admin_clients.add(websocket)  # Add to admin clients set
    try:
        async for message in websocket:
            request_data = json.loads(message)
            action = request_data.get("action")

            if action == "get_clients":
                # Send the list of connected client names
                client_names = [
                    f"Client_{client.remote_address[1]}" for client in connected_clients
                ]
                await websocket.send(
                    json.dumps({"type": "client_list", "data": client_names})
                )
            elif action == "get_messages":
                # Send the message history
                await websocket.send(
                    json.dumps({"type": "message_history", "data": message_history})
                )
            else:
                # Send the current stats
                stats = {
                    "connected_clients": len(connected_clients),
                    "total_messages": total_messages,
                }
                await websocket.send(json.dumps({"type": "stats", "data": stats}))
    except websockets.exceptions.ConnectionClosed:
        admin_clients.remove(websocket)  # Remove from admin clients set


async def update_admin_clients():
    # Broadcast updated stats to all connected admin clients
    stats = json.dumps(
        {
            "type": "stats",
            "data": {
                "connected_clients": len(connected_clients),
                "total_messages": total_messages,
            },
        }
    )
    for client in admin_clients:  # Send to admin clients only
        await client.send(stats)


async def send_message_update_to_admins(message_data):
    # Send the new message to all connected admin clients
    for admin in admin_clients:
        await admin.send(json.dumps({"type": "new_message", "data": message_data}))


start_server = websockets.serve(echo, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
