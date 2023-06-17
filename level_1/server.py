# importa os módulos necessários para fazer funções asincronas e "subir" um servidor
import asyncio
from websockets.server import serve

HOST = "localhost"
PORT = 8765

# cria uma função que será passada como parametro do server, e irá receber e enviar as mensagens
async def handleMessage(websocket):
    # envia essa mensagem para os clientes que se conectarem
    await websocket.send("Conexão WebSocket estabelecida")
    # cria um for para cada mensagem recebida de websocket
    async for message in websocket:
        # exibe a mensagem recebida dos "clientes"
        response = f"mensagem recebida pelo cliente: {message}"
        await websocket.send(response)
        print(response)

# função que sobe o websocket server
async def main():
    async with serve(handleMessage, HOST, PORT):
        await asyncio.Future() 

asyncio.run(main())