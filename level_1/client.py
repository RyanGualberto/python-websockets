# importa o módulo de conexão do websocket
from websockets.sync.client import connect

SERVER_URL = "ws://localhost:8765"
message_to_send = input("Type a message: ")

def handle_received_message(websocket):
    # cria um for para cada mensagem recebida de websocket
    for message in websocket:
        # exibe a mensagem do servidor
        print(f"Mensagem recebida do servidor: {message}")
        pass

def main():
    # Faz uma tentativa de conexão com sebsocket server na url 
    with connect(SERVER_URL) as websocket:
        # envia a mensagem para o sevidor
        websocket.send(message=message_to_send)
        handle_received_message(websocket)

try:
    main()
except KeyboardInterrupt:
    print("Encerrando.")
