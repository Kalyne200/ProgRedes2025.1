import socket

# informações para conxecão do SOCKET
host = "IP"
porta = 50000
codigo = "utf-8"


# variavel de conexão do CLIENTE SOCKET
conexao = (host,porta)


print(" *** CLIENTE SOCKET *** ")

# criando CLIENTE SOCKET
UDP_CLIENTE_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    try:
        UDP_CLIENTE_socket.bind(conexao)

        # criando mensagem para SERVIDOR SOCKET
        mensagem = input("digite sua mensagem: ")

        if not mensagem:
            break

        # envio de mensagem para SERVIDOR SOCKET
        mensagem = mensagem.encode(codigo)

        # enviando mensagem ao SERVIDOR SOCKET
        UDP_CLIENTE_socket.sendto(mensagem,conexao)

        resposta = UDP_CLIENTE_socket.recvfrom(512)

        if not resposta:
            break

        print(f" A RESPOSTA: {resposta}")

    except:
        print(f"\n Conexão encerrada pelo Cliente...")
    break


# encerrando a conexão com SERVIDOR SOCKET
UDP_CLIENTE_socket.close()
