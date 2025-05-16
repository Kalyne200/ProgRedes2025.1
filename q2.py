from hashlib import sha256
import time

''' DISCENTE: KALYNE RODRIGUES DE MELO, MATRICULA: 20232014050032'''
'''
Portanto, minerar é: a) escolher um nonce (começando de zero, por exemplo); b)
juntar com os bytes da entrada; c) calcular o hash desse conjunto; d) verificar se o
hash resultante inicia com uma certa quantidade de bits em zero; e) se o hash
calculado não atende ao requisito, repetir o processo.

Faça uma função em Python de nome findNonce que recebe dois argumentos:
dataToHash = um conjunto de bytes
bitsToBeZero = o número de bits iniciais que deve ser zero no hash
e devolve:
o nonce que satisfaz às condições
o hash encontrado
tempo (em segundos) que demorou para encontrar o nonce
'''



print(" ****BITCOINS **** ")

# NONCE DEVE COMECAR COM 20 ZEROS
# PARA SER BITCOINS

# FUNCAO INICIAL
def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

# FUNCAO PRINCIPAL
def minerar(dataToHash,transacoes,hash_anterior,bitsToBeZero):
    nonce = 0
    while True:
        texto = str(dataToHash) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
    break
        nonce += 1
    if (nonce % 10000) == 0:
        print ("Tentando nonce ", nonce)

# ATIVANDO FUNCOES
if __name__=="__main__":
    dataToHash = 15
    bitsToBeZero = 4
    hash_anterior = "abc"
    inicio = time.time()
    resultado_HASH = minerar(dataToHash,hash_anterior,bitsToBeZero)
    print(resultado_HASH)
    print(f"\n QUANTIDADE DE TEMPO DA MINERAÇÃO FOI: ")
    print(time.time() - inicio)

 # Fonte de estudo usada para desenvolver o código:
 # aulas do Hashtag treinamentos. 
