
class Operacoes():
    def __init__(self):
        True

    # não entendi o que o staticmethod faz direito, mas as funções não funcionam sem
    @staticmethod
    def soma(A, B):
        # converte os binários em inteiros
        A = int(A, 2)
        B = int(B, 2)
        
        # realiza as somas e converte o número de volta para binário
        #zfill garante q o número terá 8 bits, preenchendo o restante com 0. O retorno é uma string
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
    
    

    #definir demais funções dentro dessa Classe
    