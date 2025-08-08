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

            dados = sockCon.recv(1024)
            if not dados:
                break
            # comando recebido pelo cliente
            comando_recebido = dados.decode(code).strip()
            print(f"O comando recebido foi :{comando_recebido}")

            if comando_recebido == "DIR":
                # Listar arquivos do diretório
                listar_arquivos = os.listdir('arquivos')
                listar_arquivos = '\r\n'.join(listar_arquivos).encode('utf-8')
                sockCon.send(listar_arquivos)

            elif comando_recebido == "DOW":
                # vai receber o nome do arquivo:
                nome_do_arquivo = sockCon.recv(1024).decode(code)
                diretorio_do_arquivo = os.path.join("arquivos",nome_do_arquivo)

                # verifica se o diretorio = 'arquivos existe
                # se existir procura o nome_do_arquivo e envia
                if not os.path.exists(arquivos):
                    sockCon.send(arquivos)
                
                    # TAMANHO DO ARQUIVO RECEBIDO
                    tamanho_do_arquivo = os.path.getsize(diretorio_do_arquivo)
                    sockCon.send(str(tamanho_do_arquivo).encode(code))

                    with open(diretorio_do_arquivo,'rb') as arquivo:
                        while True:
                            dados = arquivo.read(1024)
                            if not dados:
                                break

                            sockCon.send(arquivo())

                    print(f"O arquivo foi enviado ao cliente!")
                
                else:
                    sockCon.send("ERRO: O arquivo não foi encontrado!")

            elif comando_recebido == " ":
                print("ERRO: Comando Recebido foi invalido! Vazio!")
            
            else:
                sockCon.send("ERRO: Comando enviado esta vazio! Invalido!".encode(code))
        
        
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
    threading.Thread(target=tratarCliente,args=(sockCon,origem)).start()
