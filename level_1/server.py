# importa os módulos necessários para fazer funções asincronas e "subir" um servidor
import asyncio
from websockets.server import serve

# cria uma função que será passada como parametro do server, e irá receber e enviar as mensagens
async def handleMessage(websocket):
    # envia essa mensagem para os clientes que se conectarem
    await websocket.send("Conexão WebSocket estabelecida")
    # cria um for para cada mensagem recebida de websocket
    async for message in websocket:
        # exibe a mensagem recebida dos "clientes"
        message = (f"mensagem recebida pelo cliente {message}")
        print(message)

# função que sobe o websocket server
async def main():
    async with serve(handleMessage, "localhost", 8765):
        await asyncio.Future() 

asyncio.run(main())