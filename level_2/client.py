# importa o módulo de conexão do websocket
from websockets.sync.client import connect

SERVER_URL = "ws://localhost:8765"

def handleReceivedMessage(websocket):
    # cria um for para cada mensagem recebida de websocket
    for message in websocket:
        # exibe a mensagem do servidor
        print(f"Mensagem recebida do servidor: {message}")
        pass

def handleConversation(websocket):
    # recebe um número do usuário
    number = input("Digite um número: ")
    # verifica se a entrada é um número válido
    if number.isdigit():
        # envia a mensagem para o servidor
        websocket.send(f"fatorial: {number}")
        # recebe uma mensagem do servidor
        handleReceivedMessage(websocket)  
    else:
        print("Número inválido, Tente outro número")
        pass

def main():
    # Faz uma tentativa de conexão com sebsocket server na url 
    with connect(SERVER_URL) as websocket:
        while True:
            handleConversation(websocket)
        
try:
    main()
except KeyboardInterrupt:
    print("Encerrando.")