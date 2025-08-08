import socket 
import threading
import os
import glob

print(f'\n *** SERVIDOR DE ARQUIVOS THREADING *** \n')

ip = '' 
porta = 2121 
INFO = (ip, porta)
arquivos = 'arquivos'
CODE = 'utf-8'
VARIOS = []

def escuta():
    global servidor_socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(INFO)
    servidor_socket.listen(5)
    print(f'\n SERVIDOR INICIANDO... AGUARDANDO CONEXÕES \n')
    VARIOS.append(servidor_socket)

def leitura(conexao):
    tamanho_do_comando = int.from_bytes(conexao.recv(4), byteorder='big')
    comando = b''
    while tamanho_do_comando > 0:
        leitura_comando = conexao.recv(tamanho_do_comando)
        tamanho_do_comando -= len(leitura_comando)
        comando += leitura_comando
    return comando

def adicao(dados):
    tamanho = len(dados)
    return tamanho.to_bytes(4, byteorder='big') + dados

def resposta_NULA(conexao):
    conexao.send(adicao(b''))

def resposta_DIR(conexao):
    listar_arquivos = os.listdir(arquivos)
    listar_arquivos = '\r\n'.join(listar_arquivos).encode(CODE)
    conexao.send(adicao(listar_arquivos))

def responde_DOW(nome_do_arquivo, conexao):
    nome_do_arquivo = os.path.join(arquivos, nome_do_arquivo)
    if os.path.exists(nome_do_arquivo):
        tamanho_do_arquivo = os.path.getsize(nome_do_arquivo)
        conexao.send(tamanho_do_arquivo.to_bytes(4, 'big'))

        with open(nome_do_arquivo, 'rb') as fd:
            dados = fd.read(8192)
            while dados:
                conexao.send(dados)
                dados = fd.read(8192)
    else:
        conexao.send(adicao('ERRO: Arquivo não encontrado'))

def responde_MDA(mascara, conexao):
    nomes_recebidos = 
    mascaras = mascara.split(';')
    lista_de_arquivos = []
    for m in mascaras:
        caminho = os.path.join(arquivos, m.strip())
        lista_de_arquivos.extend(glob.glob(caminho))

    num_arquivos = len(lista_de_arquivos)
    conexao.send(num_arquivos.to_bytes(4, 'big'))

    for arquivo in lista_de_arquivos:
        if os.path.exists(arquivo):
            nome_arquivo = os.path.basename(arquivo)
            conexao.send(adicao(nome_arquivo.encode(CODE)))

            tamanho_arquivo = os.path.getsize(arquivo)
            conexao.send(tamanho_arquivo.to_bytes(4, 'big'))

            with open(arquivo, 'rb') as file:
                while True:
                    pedaco = file.read(1024)
                    if not pedaco:
                        break
                    conexao.send(pedaco)

            print(f"Arquivo '{nome_arquivo}' enviado com sucesso.")

    print(f'\n Todos os arquivos foram enviados.')

def processar_comando(comando, conexao):
    if comando[:3] == b'DIR':
        resposta_DIR(conexao)
    elif comando[:3] == b'DOW':
        nome_arquivo = comando[3:].decode(CODE).strip()
        responde_DOW(nome_arquivo, conexao)
    elif comando[:3] == b'MDA':
        mascara = comando[3:].decode(CODE).strip()
        responde_MDA(mascara, conexao)
    else:
        resposta_NULA(conexao)

def tratar_cliente(conexao, cliente):
    print(f'Conexão recebida de cliente {cliente}')
    try:
        while True:
            comando = leitura(conexao)
            if not comando:
                break
            processar_comando(comando, conexao)
    except Exception as e:
        print(f'Erro com cliente {cliente}: {e}')
    finally:
        conexao.close()
        print(f'Conexão encerrada com cliente {cliente}')

def main():
    escuta()
    print(f'\n Escutando conexões...\n')
    while True:
        conexao, cliente = servidor_socket.accept()
        threading.Thread(target=tratar_cliente, args=(conexao, cliente)).start()

# ESTE CODIGO NÃO FOI APRESENTADO ONTEM EM SALA DE AULA,
# FOI FEITO APARTIR DE UM CODIGO ESCRITO NO CADERNO, PODE CONTER
# ERROS
