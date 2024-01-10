from registradores import Registradores, Memoria
from operacoes import Operacoes
import time

# faz uma instância da classe Memória. Em seguida, atribui o dicionário contido nessa classe para uma nova variável
memoria = Memoria()
mem = memoria.mem

# faz uma instância da classe Registradores. Em seguida, atribui o dicionário contido nessa classe para uma nova variável
reg = Registradores().reg



#imprime os valores atuais dos registradores e a lista de comandos, para fins de depuração
def display(reg, mem, comandos, linha_de_comando):
    return
    print("\n ******************************************************")
    print("+-----------------+")
    print("|  REGISTRADORES  |")
    print("+-----------------+")
    for i in range(0, 16):
        print(f"| {i:2} | {reg[i]} | ( {int(reg[i], 2)} )")
    print("+-----------------+")

    print("\n+-----------------+")
    print("|     MEMÓRIA     |")
    print("+-----------------+")
    for i in range(0, 5):
        print(f"| {i:2} | {mem[i]} | ( {int(mem[i], 2)} )")
    print("+-----------------+")

    # print("\n+-----------------+")
    # print("|    COMANDOS     |")
    # print("+-----------------+")
    # for chave, comando in comandos.items():
    #     print(f"| {chave:2} | {comando} |")
    # print("+-----------------+")

    print(f"\nCurrent command line: {linha_de_comando}")


# Busca os dados no endereço definido (pega cada string armazenada nos endereços do registrador)
def fetch_data(adress1, adress2):
        
        A = reg[int(adress1, 2)]
        B = reg[int(adress2, 2)]

        return A, B

def separador_de_bytes(linha):

    if(len(linha) != 28):
        print("Erro! Tamanho do comando inválido")

    comando = linha[0:4]
    adress1 = linha[4:12]
    adress2 = linha[12:20]
    adress3 = linha[20:28]

    return comando, adress1, adress2, adress3

#lê os comandos do arquivo comandos.txt e os armazena em ordem num dicionário
def le_comandos(file_path):
    comandos = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove tabs ou espaços de cada linha
    lines = [line.replace("\t", "").replace(" ", "") for line in lines]

    # Remove o caracter de nova linha
    lines = [line.strip() for line in lines]

    # Armazena cada linha num espaço do dicionário, com o número da linha como chave (começa em 1)
    for i, line in enumerate(lines, start=0):
        comandos[i] = line

    # retorna os comandos para um dicionário alvo
    return comandos


# Função principal, que executa o script
def main():

    cont = 10

    op = input("Choose operation 1, 2 or 3: ")
    
    if op == "1": 
        comandos = le_comandos('comandos.txt')
    elif op == "2":
        comandos = le_comandos('comandos2.txt')
    elif op == "3":
        comandos = le_comandos('primos.txt')

    #define o início da linha de comando como 0 (é o que controla qual comando será executado em cada ciclo. Pode ser alterado por algumas das funções de fluxo)
    linha_de_comando = 0

    # uma instância da classe operações, que contém as funções de operações
    operador = Operacoes()
    # armazenamento temporário que armazena o resultado de operações
    holder = 0

    # Imprime o status inicial da memória

    comando = "00000000"

    while linha_de_comando < len(comandos):
        # separa cada linha de comando em suas quatro partes
        comando, adress1, adress2, adress3 = separador_de_bytes(comandos[linha_de_comando])
        # imprime o status atual de cada registrador e das dez primeiras posições da memória
        display(reg, mem, comandos, linha_de_comando)
        match comando:

            # Operações de manipulação de Memória
            case "STME":
                # print(f"Armazenando em memória {(int(reg[int(adress3, 2)], 2))}")
                mem[int(reg[int(adress3, 2)], 2)] = reg[int(adress1, 2)]
                linha_de_comando += 1
            case "STRS":
                reg[int(adress1, 2)] = adress2
                linha_de_comando += 1
            case "STHR":
                reg[int(adress1, 2)] = holder
                linha_de_comando += 1
            case "GETR":
                holder = reg[int(adress1, 2)]
                linha_de_comando += 1
            case "LOAD":
                reg[int(adress1, 2)] =  mem[int(reg[int(adress3, 2)], 2)]
                linha_de_comando += 1

            # Operações Aritméticas
            case "ADD_":
                A, B = fetch_data(adress1, adress2)
                holder = operador.soma(A, B)
                linha_de_comando += 1
            case "SUB_":
                A, B = fetch_data(adress1, adress2)
                holder = operador.sub(A, B)
                linha_de_comando += 1
            case "MULT":
                A, B = fetch_data(adress1, adress2)
                holder = operador.mult(A, B)
                linha_de_comando += 1
            case "DIV_":
                A, B = fetch_data(adress1, adress2)
                holder = operador.div(A, B)
                linha_de_comando += 1

            # Operações de Fluxo
            case "JUMP":
                linha_de_comando = int(adress1, 2)
            case "JPIE":
                A, B = fetch_data(adress1, adress2)
                if(operador.jpie(A, B)):
                    linha_de_comando = int(adress3, 2)
                else:
                    linha_de_comando += 1
            case "PRNT":
                print(f" {reg[int(adress1, 2)]} = ({int(reg[int(adress1, 2)], 2)})")
                linha_de_comando += 1
            case "JPIG":
                A, B = fetch_data(adress1, adress2)
                if(operador.jpig(A, B)):
                    linha_de_comando = int(adress3, 2)
                else:
                    linha_de_comando += 1
            case "END_":
                print("FIM DO SCRIPT")
                linha_de_comando += 1000
                break
            case "FILL":
                linha_de_comando += 1
                pass
            case _:
                print(f"Invalid command: {comando}")
                linha_de_comando += 1
        
        if(int(reg[5], 2) == 101): cont -= 1
        # if(cont == 0): break
        # espera algum tipo de inputentre cada operação. Remover na versão final
        # step = input('')


# força a execução da função main. Não é necessário em C
if __name__ == "__main__":
    main()
