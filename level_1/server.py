#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    await websocket.send("Conexão WebSocket estabelecida")
    async for message in websocket:
        message = (f"mensagem recebida pelo cliente {message}")
        await websocket.send(message)
        print(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future() 

asyncio.run(main())