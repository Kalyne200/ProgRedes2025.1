import socket
import threading
import os

ip = '127.0.0.1'
porta = 2121
pasta_arquivos = 'arquivos'
code = 'utf-8'

print("\n*** CLIENTE DE ARQUIVOS MULTITHREADING ***\n")

# Criar socket global
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((ip, porta))

def tratarUsuario():
    while True:
        print("\n1 - Listar arquivos no servidor")
        print("2 - Download de um arquivo")
        print("3 - Download de múltiplos arquivos")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cliente_socket.send("DIR".encode(code))
        elif opcao == '2':
            nome_do_arquivo = input("Digite o nome do arquivo: ")
            cliente_socket.send(f"DOW|{nome_do_arquivo}".encode(code))
        elif opcao == '3':
            nomes = input("Digite os nomes dos arquivos separados por vírgula: ")
            cliente_socket.send(f"DMA|{nomes}".encode(code))
        elif opcao == '4':
            cliente_socket.send("FIM".encode(code))
            break
        else:
            print("Opção inválida. Tente novamente.")

def tratarServidor():
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)
        print(f"Diretório '{pasta_arquivos}' foi criado.")

    while True:
        try:
            resposta = cliente_socket.recv(1024).decode(code)
            if resposta.startswith("LISTA|"):
                arquivos = resposta[6:].split(',')
                print("\nArquivos disponíveis no servidor:")
                for arq in arquivos:
                    print(f" - {arq}")
            elif resposta.startswith("ARQUIVO|"):
                partes = resposta.split('|')
                nome = partes[1]
                tamanho = int(partes[2])
                print(f"Recebendo arquivo: {nome} ({tamanho} bytes)")

                caminho = os.path.join(pasta_arquivos, nome)
                with open(caminho, 'wb') as f:
                    recebido = 0
                    while recebido < tamanho:
                        dados = cliente_socket.recv(min(1024, tamanho - recebido))
                        if not dados:
                            break
                        f.write(dados)
                        recebido += len(dados)
                print(f"Arquivo '{nome}' salvo em '{pasta_arquivos}'")
            elif resposta == "FIM":
                print("Conexão encerrada pelo servidor.")
                break
            else:
                print(f"Resposta desconhecida: {resposta}")
        except Exception as e:
            print(f"Erro na comunicação com o servidor: {e}")
            break

# Iniciar as threads
thread_usuario = threading.Thread(target=tratarUsuario)
thread_servidor = threading.Thread(target=tratarServidor)

thread_usuario.start()
thread_servidor.start()

thread_usuario.join()
thread_servidor.join()

cliente_socket.close()
