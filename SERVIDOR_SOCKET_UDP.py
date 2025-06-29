import socket

# informações do SOCKET
porta = 50000
my_conexao = ("IP",porta) # my_conexao = " "-> ip do servidor,porta -> porta do servidor
all_Clientes = [] # lista de clientes

print(f" **** SERVIDOR SOCKET **** ")

# criando o SERVIOR SOCKET
SERVIDOR_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# TRY -> VERIFICA POSSIVEIS ERROS DE CONEXAO, 
# RECEBIMENTO E ENVIO DE MENSAGENS NO SERVIDOR SOCKET
try:
    SERVIDOR_socket.bind(my_conexao)
    while True:
        try:
            DADOS,FONTE = SERVIDOR_socket.recvfrom(512)
            print(f"OK! Recebido! {FONTE}:{DADOS.decode()}")
            if FONTE not in all_Clientes: # if fonte not in all_clientes
                all_Clientes.append(FONTE)
            for cliente in all_Clientes:
                if FONTE != cliente:
                    SERVIDOR_socket.sendto(DADOS,FONTE)
        except:
            print(f" *** ERRO: Processamento da mensagem. *** ")
    socket.close() # ESTA DESATIVO, NO ENTANTO O CLOSE TEM FUNCAO DE ENCERRAR CONEXAO SOCKET
except:
    print(f" *** ERRO: Verifique se a porta {porta} não esta em uso. ***")
