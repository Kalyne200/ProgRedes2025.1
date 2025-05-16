import struct

def ler():
    try:
        diretorio = "pes.jpg"
        # diretorio = " INFORME AQUI DIRETORIO DA SUA IMAGEM"
        with open (diretorio, "rb") as app1DataSize:
            objeto = app1DataSize.read()
        # leitura do arquivo 1: "app1DataSize"
        
        tamanho = None # tamanho dos metadados
        if len(objeto) >= 6:
            header = objeto[:6]
            tamanho = struct.unpack(">H", header[4:6])[0]
            print(f"tamanho do arquivo app1DataSize é: {tamanho}")
    except TypeError as e:
            print("Erro ao ler tamanho dos metadados: Arquivo muito curto {e}.")
            # obs consudera-se 6 bytes, mas le apenas os bytes 4 - 5

            with open (diretorio, "rb") as app1DataSize:
                objeto = app1DataSize.read()

            if len(objeto) >= 4:
                header_2 = objeto[:4]
                tamanho = struct.unpack(">H", header_2[2:4])[0]
                print(f" INGNORE!!")
    except TypeError as e:
        print("Erro ao ler tamanho dos metadados: Arquivo muito curto. {e}")

    largura = 0x0100 # (Largura)
    altura = 0x0101 # (Altura)
    orientacao = 0x0112 # (Orientação)
    modelo_foto = 0x010E # (Modelo)
    tamanho = 20

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


if __name__ == "__main__":
    ler()






