import subprocess

def abrir(arquivo):

# abertura e leitura do arquivo 
    arquivo = open("imagem.jpg","rb")
    arquivo.read()
    #arquivo.close()
    print(arquivo)

# imprime o nome do arquivo
    if len(sys.argv) < 2:
        print (f"uso: {sys.argv[0]} nome do arquivo: {arquivo}")
        sys.exit(1)

# verifica erros nos comandos 
    try:
       subprocess.run(["start", arquivo], shell=True, check=True) 

    except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
        except subprocess.CalledProcessError:
            print("Erro ao tentar abrir o navegador.")
    
    site = https://www.openstreetmap.org/#map=4/-15.13/-53.19
    abrir(site)


