#!/usr/bin/env python

import asyncio
from websockets.server import serve

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# async def client_callback(message, websocket):
    

async def echo(websocket):
    await websocket.send("Conexão WebSocket estabelecida")
    async for message in websocket:
        if message.startswith("fatorial:"):
            number = int(message.split(":")[1])
            if number >= 0:
                result = calcular_fatorial(number)
                response = f"O fatorial de {number} é {result}"
                await websocket.send(response)
                print(response)
            else:
                await websocket.send("Número inválido. Por favor, envie um número inteiro positivo.")
        else:
            message = f"mensagem recebida pelo cliente {message}"
            await websocket.send(message)
            print(message)
        

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future() 

asyncio.run(main())