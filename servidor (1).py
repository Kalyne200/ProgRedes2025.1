import socket
import threading
import os

ip = 'localhost' # ou 127.0.0.1'
porta = 2121 # ou 50000

code = "utf-8"
arquivos = "arquivos"

allClientes = []

print(f"\n SERVIDOR SOCKET DE ARQUIVOS COM THREAD \n")

def tratarCliente(sockCon,origem):
    try:
        print(f"Tratar conexao com :{origem}")
        
        allClientes.append(sockCon)
        while True:
            comando = sockCon.recv(1024).decode(code)
            print('recebi de {origem} -> {comando.sockCon()}')
            for servidor_socket in allClientes:
                if servidor_socket!=  sockCon:
                    servidor_socket(comando)

                    if comando[:3] == "DIR":
                        listar_arquivos = os.listdir(arquivos)
                        listar_arquivos = '\r\n'.join(listar_arquivos).encode()
                        conexao.send(listar_arquivos)
                    
                    elif comando == "DOW":
                        nome = "DOW" + arquivos + "/"
                        tamanho_arquivo = os.path.getsize(nome)
                        sockCon.recv(tamanho_arquivo.decode(code))

                        with open(nome,'rb') as arquivo:
                            dados = arquivo.read(8192)
                            while(dados != b" "):
                                sockCon.send(dadps)
                                dados = aequivo.read(8191)
                                
                    else:
                        if comando == " ":
                            print(f" O comando esta vazio! Invalido")

    except:                  
        allClientes.remove(sockCon)
        sockCon.close()
        print("ENCERRANDO CONEXÃO")

servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind((ip,porta))
servidor_socket.listen(5)

while True:
    print(f'\n Aguardando conexão.....')
    sockCon,origem = servidor_socket.accept()
    threading.Thread(target=tratar_cliente,args=(sockCon,origem)).start()
