import sys


arquivo = open("sapatos.jpg","rb")
arquivo.close()
print(arquivo)


if len(sys.argv) < 2:
    print (f"uso: {sys.argv[0]} nome do arquivo: {arquivo}")
    sys.exit(1)



