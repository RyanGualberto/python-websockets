# importa os módulos necessários para fazer funções asincronas e "subir" um servidor
import asyncio
from websockets.server import serve

# calcula o fatorial de n
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)    

# cria uma função que será passada como parametro do server, e irá receber e enviar as mensagens
async def handleMessage(websocket):
    # envia essa mensagem para os clientes que se conectarem
    await websocket.send("Conexão WebSocket estabelecida")
    # cria um for para cada mensagem recebida de websocket
    async for message in websocket:
        # se a mensagem conter "fatorial", passas para o bloco de calculo fatorial
        if message.startswith("fatorial:"):
            # extrai o número da mensagem
            number = int(message.split(":")[1])
            # caso o número seja maior que 0, faz o calculo e imprime no servidor
            if number >= 0:
                result = calcular_fatorial(number)
                response = f"O fatorial de {number} é {result}"
                await websocket.send(response)
                print(response)
            # caso o número seja menor que 0 imprime que é um número inválido
            else:
                await websocket.send("Número inválido. Por favor, envie um número inteiro positivo.")
        # caso a mensagem não contenha a palavra fatorial apenas, mostra a mensagem enviada pelo cliente                
        else:
            message = f"Comando não reconhecido: {message}"
            await websocket.send(message)
            print(message)
        

# função que sobe o websocket server
async def main():
    async with serve(handleMessage, "localhost", 8765):
        await asyncio.Future() 

asyncio.run(main())