import struct

# INFORME UM ENDEREÇO IPV4
ip4 = input("digite: ")
#digite: 200.17.143.131 - ENDEREÇO INFORMADO APENAS PARA TESTE
# ------------------------------------------------------------------------------------------------------------
# INFORME UMA MASCARA IPV4
mask = int(input("digite: "))
#digite: 18 - MASCARA INFORMADA APENAS PARA TESTE
# ------------------------------------------------------------------------------------------------------------

# O IP E UM NUMERO DE 32 BITS
# | = OU

# ------------------------------------------------------------------------------------------------------------
bitsHosts = 32 - mask

ip = 0
for num in ip4.split("."):
    ip = (ip << 8) | int(num)


End_REDE = (ip >> bitsHosts) << bitsHosts # endereco de rede em bits
End_BROAD = End_REDE | ((1 << bitsHosts) - 1) # endereco de broadcast em bits
End_GTW = End_REDE | 1 # endereco do gateway em bits

print(f"\n O ENDEREÇO IP DA REDE É: {End_REDE}")
print(f"\n O ENDEREÇO BROADCAST DA REDE É: {End_BROAD}")
print(f"\n O ENDEREÇO DE GATEWAY DA REDE É: {End_GTW}")
print(f"#------------------------------------------------------------------------------------------")
print(f"\n O ENDEREÇO DE REDE É: {End_REDE}")
print(f"\n O ENDEREÇO DE BROADCAST É: {End_BROAD}")
print(f"#------------------------------------------------------------------------------------------")
# -------------------------------------------------------------------------------------------------------------

# INFORMAÇÕES:
# CONJUNTO ARRAY DE INTEIROS
# End_REDE_array = bytearray([200,17,143,131])

# --------------------------------------------------------------------------------------------------------------
print(f"\n ***** BYTES DO ENDEREÇO DE REDE *****")
print(f"#------------------------------------------------------------------------------------------")

# EM FORMATO BIG - ENDIAN
End_REDE_BIG = struct.pack(">I",End_REDE)
# EM FORMATO LITTLE - ENDIAN 
End_REDE_LITTLE = struct.pack("<I",End_REDE)

End_REDE_1 = struct.unpack("BBBB",End_REDE_BIG)
End_REDE_2 = struct.unpack("BBBB",End_REDE_LITTLE)

print(f"\n ENDEREÇO DE REDE EM FORMATO BIG - ENDIAN: {End_REDE_1}")
print(f"\n ENDEREÇO DE REDE EM FORMATO LITTLE - ENDIAN: {End_REDE_2}")

 # TEM UM ERRO AQUI --------------------------------------------
bytes_rede = struct.unpack("BBBB",End_REDE)
print(bytes_rede)
# ------------------------------------------------------------------------------

print(f"#------------------------------------------------------------------------------------------")
print(End_REDE_bytes1[0],End_REDE_bytes1[1],End_REDE_bytes1[2],End_REDE_bytes1[3])

# -------------------------------------------------------------------------------------------------------------------------------------------
print(f"#------------------------------------------------------------------------------------------")
print(f"\n ***** BYTES DO ENDEREÇO DE BROADCAST ***** ")

# EM FORMATO BIG - ENDIAN
End_BROAD_BIG = struct.pack(">I",End_BROAD)
# EM FORMATO LITTLE - ENDIAN 
End_BROAD_LITTLE = struct.pack("<I",End_BROAD)

End_BROAD_1 = struct.unpack("BBBB",End_BROAD_BIG)
End_BROAD_2 = struct.unpack("BBBB",End_BROAD_LITTLE)

print(f"\n ENDEREÇO DE BROADCAST EM FORMATO BIG - ENDIAN: {End_BROAD_1}")
print(f"\n ENDEREÇO DE BROADCAST EM FORMATO LITTLE - ENDIAN {End_BROAD_2}")
print(f"#------------------------------------------------------------------------------------------")

# INFORMAÇÕES IMPORTANTES:
# Big-Endian (>): O byte mais significativo vem primeiro. 
# É a ordem padrão para dados de rede.
# Little-Endian (<): O byte menos significativo vem primeiro. 
# É comum em algumas arquiteturas de processadores (como x86).
