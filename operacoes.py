
class Operacoes():
    def __init__(self):
        True

    @staticmethod
    def soma(A, B):
        # converte os binários em inteiros
        A = int(A, 2)
        B = int(B, 2)
        
        # realiza as somas e converte o número de volta para binário
        soma = bin(A + B)[2:].zfill(8)
        return soma
    
    @staticmethod
    def sub(A, B):
        # converte os binários em inteiros
        A = int(A, 2)
        B = int(B, 2)
        
        # realiza as somas e converte o número de volta para binário
        sub = bin(A - B)[2:].zfill(8)
        return sub