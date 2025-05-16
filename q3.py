import struct

# --- FUNÇÃO DE LEITURA DE ABERTURA E LEITURA DE ARQUIVOS ---
def ler():
    try:
        diretorio = "sapatos.jpg" # INFORME AQUI O NOME DA SUA IMAGEM
        # diretorio = " INFORME AQUI DIRETORIO DA SUA IMAGEM"
        with open (diretorio, "rb") as app1DataSize:
            objeto = app1DataSize.read()
        # leitura do arquivo 1: "app1DataSize"
        
        tamanho = None # tamanho dos metadados
        
        if len(objeto) >= 6:
            header_1= objeto[:6]
            tamanho = struct.unpack(">H", header_1[4:6])[0]
            print(f"tamanho do arquivo app1DataSize é: {tamanho}")
            
    except TypeError as e: # realiza a verificação de possiveis erros na leitura dos bytes
            print("Erro ao ler tamanho dos metadados: Arquivo muito curto {e}.")
            # obs consudera-se 6 bytes, mas le apenas os bytes 4 - 5

            with open (diretorio, "rb") as app1DataSize:
                objeto = app1DataSize.read()

            if len(objeto) >= 4:
                header_2 = objeto[:4]
                tamanho = struct.unpack(">H", header_2[2:4])[0]
                print(f" INGNORE!!")
            # ingora os 4 bytes nas posições 2 e 4

            if len(objeto) >= 18:
                header = objeto[:18]
                tamanho = struct.unpack(">H", header[16:18])[0]
                print(f"tamanho do arquivo app1DataSize é: {tamanho}")
                
    except TypeError as e:  # realiza a verificação de possiveis erros na leitura dos bytes
        print("Erro ao ler tamanho dos metadados: Arquivo muito curto {e}.")
    # obs consIdera-se os bytes apartir da posição 18

    # --- LER METADADOS ESPECÍFICOS ---

    # Posições dos metadados (convertidas para decimal) AQUI SERA USADA APENAS AS INFORMACÇ~EOS EM HEXA : 
    # 0X100 PARA DESCUBRIR A POSICAO, LARGURA, ORIENTAÇAÕ E MODELO E EM SEGUIDA O VALOR DOS METADADOS
    # INDENTIFICADORES DE POSIÇÕES:
    
    largura = 0x0100 # (Largura)
    altura = 0x0101 # (Altura)
    orientacao = 0x0112 # (Orientação)
    modelo_foto = 0x010E # (Modelo)
    tamanho = 20

    # --- FUNÇÃO DE EXTRAÇÃO DE METADADOS ---
    def extrair(data, posicao, tipo):
        try: # VERIFICANDO POSSIVEIS ERROS...
            tamanho_tipo = struct.calcsize(tipo)
            if posicao + tamanho_tipo > len(data):
                raise IndexError(f"Posição {posicao} fora dos limites")
            valor_bytes = data[posicao:posicao + tamanho_tipo]
            return struct.unpack(tipo, valor_bytes)[0]
        except IndexError as e:
            print(f"Erro ao ler na posição {posicao}: {e}")
            return None
        except struct.error as e:
            print(f"Erro ao descompactar na posição {posicao}: {e}")
        return None

    # DADOS EMPACOTADOS NO FORMATO BIG - ENDIAN
    largura = extrair(objeto, largura, '>H')
    altura = extrair(objeto, altura, '>H')
    orientacao = extrair(objeto, orientacao, '>H')

    modelo = "Modelo não encontrado"

# VERFICANDO POSSIVEIS ERROS NA LEITURA DOS INDENTIFICADORES DE POSIÇÕES 
    try:
        if modelo_foto + tamanho <= len(objeto):
            modelo_bytes = objeto[modelo : modelo_foto + tamanho]
            modelo = modelo_bytes.decode('utf-8', errors='ignore').rstrip('\x00')
        else:
            print(f"Aviso: Posição do modelo ({modelo_foto}) fora dos limites.")
    except Exception as e:
        print(f"Erro ao decodificar o modelo: {e}")

        print("\n***** METADADOS ENCONTRADOS *****")
        print(f"Largura: {largura}")
        print(f"Altura: {altura}")
        print(f"Orientação: {orientacao}")
        print(f"Modelo: {modelo_foto}")

    # VERIFICANDO POSSIVEIS ERROS NO ARQUIVO:
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- ATIVANDO A FUNÇÃO PRINCIPAL: "ler" ---
if __name__ == "__main__":
    ler()

# IMFORMÇÕES:

# OBSERVAÇÃO 1:
# IMAGEM "SAPATOS" UTILIZADA NA RESOLUÇÃO, E A MESMA IMAGEM DISPONIBILIZADA PELO
# PROFESSOR NO GOOGLE SALA DE AULA, O ARQUIVO TAMBÉM FOI TESTADO COM CAMINHO DO 
# DIRETORIO 

# OBSERVAÇÃO 2:
# Faça um programa que leia os primeiros 6 bytes da imagem JPEG em anexo. Nas
#posições 4 e 5 há um valor que especifica o tamanho dos metadados presentes nessa
#imagem. Obtenha esse número (chame-o app1DataSize). Feche o arquivo.
#a) Abra o arquivo novamente, leia 4 bytes e os ignore. Agora leia o número de
#bytes em app1DataSize para app1Data. Na posição 16 de app1Data
#há 2 bytes que indicam quantos metadados essa imagem tem. Descubra-o e
#informe.

# A PRIMEIRA PARTE DO ARQUIVO REFERENTE A FUNÇÃO: "ler"
# REALIZA A ABERTURA E LEITURA DO ARQUIVO E SEUS PRIMEIROS 6 BYTES, NAS POSIÇÕES 4 E 5
# DEPOIS FECHA (COMO USEI WITH OPEN, NÃO FORA USADA CLOSE, APENAS PRINT PARA FORNECER 
# INFORMAÇÕES
# DEPOIS ELE ABRI NOVAMENTE O ARQUIVO E LÊ MAIS 4 BYTES, E INGNORA
# APARTIR DA POSIÇÃO 18 A FUNÇÃO EXTRAI OS METADADOS USANDO AS INFORMAÇÕES DOS 
# INDENTIFICADORES DE POSIÇÕES (ESSAS INFORMAÇÕES FORAM RETIRADAS DO ARQUIVO:
# https://exiftool.org/TagNames/EXIF.html

# OS BYTES SÃO EMPACOTADOS EM FORMATO BIG - ENDIAN
# DEPOIS SÃO DECODIFICADOS, SAINDO DO FORMATO BYTES PARA O FORMATO STRING, 
# VERIFICANDO POSSIVEIS ERROS NESSE PROCESSO

# EM SEGUIDA A IMPRESSÃO DAS INFORMAÇÕES COM "print"

# VERFICAÇÃO DE ERROS NO ARQUIVO (IMAGEM)
#  E POR ULTIMO A ATIVAÇÃO "ler" 










