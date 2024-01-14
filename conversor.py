import struct



# Funções responsáveis pela conversão de binário para float e vice-versa


def binary32_to_float(binary_string):
    # Converte a string binária para sua representação de 32 bits como inteiro
    representacao_binaria = int(binary_string, 2)

    # Desempacota a representação de 32 bits para obter o número de ponto flutuante
    valor_flutuante = struct.unpack('!f', struct.pack('!I', representacao_binaria))[0]

    return valor_flutuante


def float_to_binary32(f):
    # Converte o número de ponto flutuante para sua representação de 32 bits
    representacao_binaria = struct.unpack('!I', struct.pack('!f', f))[0]

    # Converte a representação de 32 bits para uma string binária
    string_binaria = bin(representacao_binaria)[2:].zfill(32)

    return string_binaria
