from math import ceil
from conversor import binary32_to_float, float_to_binary32
import struct

class Operacoes():
    def __init__(self):
        True


    # não entendi o que o staticmethod faz direito, mas as funções não funcionam sem
    @staticmethod
    def soma(A, B):
        # converte os binários em inteiros

        A = binary32_to_float(A)
        B = binary32_to_float(B)
        
        # realiza a soma e converte o número para um float 32 bits
        soma = float_to_binary32(A+B)
        return soma
    
    
    @staticmethod
    def sub(A, B):
        # converte os binários em inteiros
        A = binary32_to_float(A)
        B = binary32_to_float(B)
        
        # realiza a subtração e converte o número para um float 32 bits
        sub = float_to_binary32(A-B)
        return sub
    
    @staticmethod
    def mult(A, B):
        # converte os binários em float
        A = binary32_to_float(A)
        B = binary32_to_float(B)

        mult = float_to_binary32(A*B)
        return mult
    
    @staticmethod
    def div(A, B):
        # converte os binários em float
        A = binary32_to_float(A)
        B = binary32_to_float(B)

        # Perform the division
        result = A / B

        # Convert the result to a 32-bit binary string
        result_binary = float_to_binary32(result)

        return result_binary
    
    @staticmethod
    def remainder(A, B):
        # converte os binários em inteiros

        A = binary32_to_float(A)
        B = binary32_to_float(B)

        A = int(A)
        B = int(B)

        div = float((A%B))
        div = float_to_binary32(div)
        return div
    
    @staticmethod
    def power(A, B):
        # converte os binários em inteiros

        A = binary32_to_float(A)
        B = binary32_to_float(B)
        
        A = int(A)
        B = int(B)

        power = float((pow(A, B)))

        power = float_to_binary32(power)
        return power
    
    @staticmethod
    def factorial(A):
        # converte os binários em inteiros
        A = int(binary32_to_float(A))

        fac = 1

        for i in range(1, A+1):
            fac = fac * i

        fac = float(fac)    
        return float_to_binary32(fac)
    
    @staticmethod
    def jpie(A, B):
        # converte os binários em inteiros
        A = binary32_to_float(A)
        B = binary32_to_float(B)
        
        A = int(A)
        B = int(B)
        if(A == B): return True
        else: return False

    @staticmethod
    def jpig(A, B):
        # converte os binários em inteiros
        A = binary32_to_float(A)
        B = binary32_to_float(B)
        
        A = int(A)
        B = int(B)

        if(A > B): return True
        else: return False

    
