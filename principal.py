from registradores import Registradores, Memoria
from operacoes import Operacoes

memoria = Memoria()
mem = memoria.mem
reg = Registradores().reg



#imprime os valores atuais dos registradores e a lista de comandos, para fins de depuração
def display(reg, mem, comandos, linha_de_comando):
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
    for i in range(0, 10):
        print(f"| {i:2} | {mem[i]} | ( {int(mem[i], 2)} )")
    print("+-----------------+")

    print("\n+-----------------+")
    print("|    COMANDOS     |")
    print("+-----------------+")
    for chave, comando in comandos.items():
        print(f"| {chave:2} | {comando} |")
    print("+-----------------+")

    print(f"\nCurrent command line: {linha_de_comando}")


# Busca os dados no endereço definido
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

    # Remove empty spaces from each line
    lines = [line.replace(" ", "") for line in lines]
    # Remove o caracter de nova linha
    lines = [line.strip() for line in lines]

    # Armazena cada linha num espaço do dicionário, com o número da linha como chave (começa em 1)
    for i, line in enumerate(lines, start=0):
        comandos[i] = line

    # retorna os comandos para um dicionário alvo
    return comandos



def main():


    op = input("Choose operation 1 or 2: ")
    
    if op == "1": 
        comandos = le_comandos('comandos.txt')
    elif op == "2":
        comandos = le_comandos('comandos2.txt')
    linha_de_comando = 0

    operador = Operacoes()
    holder = 0

    # Imprime o status inicial da memória

    comando = "00000000"

    while linha_de_comando < len(comandos) - 1:
        comando, adress1, adress2, adress3 = separador_de_bytes(comandos[linha_de_comando])
        display(reg, mem, comandos, linha_de_comando)
        match comando:

            # Memória
            case "STME":
                mem[int(adress3, 2)] = reg[int(adress1, 2)]
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
                reg[int(adress3, 2)] = mem[int(adress1, 2)]
                linha_de_comando += 1

            # Aritméticos
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

            # Fluxo
            case "JUMP":
                linha_de_comando = int(adress1, 2)
            case "JPIE":
                B = reg[int(adress1, 2)]
                if(operador.jpie(holder, B)):
                    linha_de_comando = int(adress3, 2)
                else:
                    linha_de_comando += 1
            case "PRNT":
                print(f"Valor armazenado no endereço {int(adress1, 2)} : {reg[int(adress1, 2)]} = ({int(reg[int(adress1, 2)], 2)})")
                linha_de_comando += 1
            case "JPIG":
                B = reg[int(adress1, 2)]
                if(operador.jpig(holder, B)):
                    linha_de_comando = int(adress3, 2)
                else:
                    linha_de_comando += 1
            case "END_":
                print("FIM DO SCRIPT")
                linha_de_comando += 1
                break
            case _:
                print(f"Invalid command: {comando}")
                linha_de_comando += 1
        



if __name__ == "__main__":
    main()



# verificar se a memória está funcionando
# criar uma variável q serve de controle para em qual linha de comando estamos