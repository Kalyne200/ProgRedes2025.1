import socket
import threading
import os

ip = '127.0.0.1'
porta = 2121
arquivos = 'arquivos'
code = 'utf-8'

print("\n*** CLIENTE DE ARQUIVOS MULTITHREADING ***\n")

def tratarUsuario():
    global nome_do_arquivo

    print ("1 - Lista arquivos no servidor")
    print ("2 - Donwload de um arquivo")
    print ("3 - Download de mais de uma arquivo")
    print ("4 - Fim")
    return int (input("Escolha uma opção: "))

    nome_do_arquivo = str(input("Digite o nome do comando: "))
    cliente_socket.send(nome_do_arqiuivo.encode(code))
    
def tratarServidor():

    while True:
        
        comando = "DIR"
        cliente_socket.send(comando.encode(code))
        if os.path.exists(arquivos):
            os.makdirs(arquivos)
            print("diretorio {arquivso} foi criado")

            nome_do_arquivo_recebido = cliente_socket.recv(1024).encode(code)
            diretorio_do_arquivo = cliente_socket("arquivos",nome_do_arquivo_recebido)

            tamanho_da_lista = cliente_socket.recv(diretorio_do_arquivo.decode())
            while tamanho_da_lista > 0:
                resposta = cliente_socket.recv(tamanho_da_lista)
                tamanho_da_lista -= len(resposta)
                primt(resposta.decode())
            return
        
        comando = "DOW"
        client_socket.send(comando.encode(code))

        nome_do_arquivo_recebido = cliente_socket.recv(1024).decode(code)
        diretorio_do_arquivo = cliente_socket("arquivos",nome_do_arquivo_recebido)

        tamanho_do_arquivo = os.path.getsize(nome_do_arquivo)

        dados_do_arquivo = cliente_socket.recv(1024)
        
        while tamanho_do_arquivo > 0:
            leitura = cliente_socket.recv(tamanho_do_arquivo).decode()
            tamanho_do_arquivo -= (leitura)
        
        comando = "DMA"
        cliente_socket.send(coamndo.encode(code))
        

        nome_do_arquivo = nome_do_arquivo_bytes.decode(code).strip()
        print(f"Recebendo arquivo: {nome_do_arquivo}")

    cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente_socket.connect((ip,porta))

    thread_usuario = threading.Thread(target = tratarUsuario)
    thread_servidor = threading.Thread(target = tratarServidor)

    thread_usuario.start()
    thread_servidor.start()

    thread_usuario.join()
    thread_servidor.join()

    cliente_socket.close()
