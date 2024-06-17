import asyncio
import websockets
import json


async def admin_handler(websocket, path):
    while True:
        try:
            # Read stats from the file
            with open("stats.json", "r") as stats_file:
                stats = json.load(stats_file)
            await websocket.send(json.dumps(stats))
        except FileNotFoundError:
            # If the stats file does not exist, initialize with zeros
            await websocket.send(
                json.dumps({"connected_clients": 0, "total_messages": 0})
            )
        await asyncio.sleep(1)  # Update every second.


async def main():
    async with websockets.serve(admin_handler, "localhost", 6790):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
