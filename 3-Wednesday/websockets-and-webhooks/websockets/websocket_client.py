import asyncio
import websockets


async def hello():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, World!")
        response = await websocket.recv()
        print(f"Received from server: {response}")


# Use asyncio.run() to run the hello coroutine
asyncio.run(hello())
