# importa o módulo de conexão do websocket
from websockets.sync.client import connect

def main():
    # Faz uma tentativa de conexão com sebsocket server na url 
    with connect("ws://localhost:8765") as websocket:
        # envia a mensagem para o sevidor
        websocket.send("Hello world!")
        # recebe uma mensagem do servidor
        message = websocket.recv()
        # exibe a mensagem do servidor
        print(f"Received: {message}")

main()