# importa o módulo de conexão do websocket
from websockets.sync.client import connect

SERVER_URL = "ws://localhost:8765"
number = input("Type a number: ")

def main():
    # Faz uma tentativa de conexão com sebsocket server na url 
    with connect(SERVER_URL) as websocket:
        # envia a mensagem para o sevidor
        websocket.send(f"fatorial: {number}")
        # recebe uma mensagem do servidor
        message = websocket.recv()
        # exibe a mensagem do servidor
        print(f"Received: {message}")

main()