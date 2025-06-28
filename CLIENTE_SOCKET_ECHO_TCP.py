import socket

# informações para conxecão do SOCKET
HOST = "INFORME AQUI O SEU IP"
PORT = 50000
CODE = "utf-8"

# variavel de conexão do CLIENTE SOCKET 
CONEXAO = (HOST,PORT)

print(f"\n  *** CLIENTE SOCKET ECHO TCP *** ")

# CRIANDO O  CLIENTE_SOCKET_ECHO_TCP
CLIENTE_TCP_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# LOOP INFINITO DA CONEXÃO
while True:
    try:

        CLIENTE_TCP_SOCKET.connect(CONEXAO)
        # CONEXAO, SERVIDOR = CLIENTE_TCP_SOCKET.connect()

        print(f"\n INICIANDO CONEXÃO CLIENTE SOCKET ECHO TCP ... {CLIENTE_TCP_SOCKET}")

        # LOOP DETERMINADO DA CONEXAO
        # DETERMINANDO QUANTIDADE DE ENVIOS DE MENSAGENS
        for indice in range(5):
            
            # MENSAGEM = input("digite sua mensagem: ")
            MENSAGEM = "OLA! BUENAS NOCHES! "

            # CONVERTENDO STRINGS EM BYTES
            MENSAGEM = MENSAGEM.encode(CODE)

            # ENVIANDO MENSAGENS PARA O SERVIDOR_SOCKET_ECHO_TCP
            CLIENTE_TCP_SOCKET.send(MENSAGEM,CONEXAO)
    
            # RECEBENDO RESPOSTA DO SERVIDOR_SOCKET_ECHO_TCP
            RESPOSTA = CLIENTE_TCP_SOCKET.recv(1024).decode()

            # IMPRIMINDO RESPOSTA DO SERVIDOR_SOCKET_ECHO_TCP
            print(f"\n RESPOSTA DO SERVIDOR: {RESPOSTA}")

    except:

        # CONEXAO.close()

        # ENCERRANDO O LOOP DETERMINADO DA CONEXÃO 
        print(f"\n CONEXÃO FINALIZADA: {CONEXAO}")

        # ENCERRANDO O CLIENTE_SOCKET_ECHO_TCP
        CLIENTE_TCP_SOCKET.close()
