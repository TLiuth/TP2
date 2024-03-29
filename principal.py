from registradores import Registradores, Memoria
from operacoes import Operacoes
import time
from conversor import binary32_to_float, float_to_binary32


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
        print(f"| {i:2} | {reg[i]} | ( {binary32_to_float(reg[i])} )")
    print("+-----------------+")

    print("\n+-----------------+")
    print("|     MEMÓRIA     |")
    print("+-----------------+")
    for i in range(0, 5):
        print(f"| {i:2} | {mem[i]} | ( {binary32_to_float(mem[i])} )")
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

# Separa a linha de comando em partes
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

    
    while(1):
        op = input("Escolha a operação 1 (primos) ou 2 (cálculo de sen e cos): ")
        if op == "1": 
            comandos = le_comandos('primos.txt')
        elif op == "2":
            comandos = le_comandos('sencos.txt')
            rad = float(input("Entre um valor em radianos: "))
            reg[2] = float_to_binary32(rad)
        else:
            print("Opção inválida. Tente novamente")
        if(op == "1" or op == "2"): break

    #define o início da linha de comando como 0 (é o que controla qual comando será executado em cada ciclo. Pode ser alterado por algumas das funções de fluxo)
    linha_de_comando = 0

    # uma instância da classe operações, que contém as funções de operações
    operador = Operacoes()
    # armazenamento temporário que armazena o resultado de operações
    holder = 0

    st = time.process_time()

    while linha_de_comando < len(comandos):
        # separa cada linha de comando em suas quatro partes
        comando, adress1, adress2, adress3 = separador_de_bytes(comandos[linha_de_comando])

        # imprime o status atual de cada registrador e das dez primeiras posições da memória
        display(reg, mem, comandos, linha_de_comando)

        # Controla o fluxo dos scripts
        match comando:

            # Operações de manipulação de Memória
            case "STME":
                # pega o valor armazenado no registrador, transforma para float, e então para int, para ser usado como chave
                endereco = reg[int(adress3, 2)]
                endereco = binary32_to_float(endereco)
                endereco = int(endereco)

                # armazena na memória com chave endereço o conteúdo do registrador adress1
                mem[endereco] = reg[int(adress1, 2)]
                linha_de_comando += 1

            case "STRS":
                # pega o valor inteiro de adress2, converte para float, e armazena no registrador adress1
                conteudo = float(int(adress2, 2))
                conteudo = float_to_binary32(conteudo)

                reg[int(adress1, 2)] = conteudo
                linha_de_comando += 1

            case "STHR":
                reg[int(adress1, 2)] = holder
                linha_de_comando += 1

            case "GETR":
                holder = reg[int(adress1, 2)]
                linha_de_comando += 1
            case "LOAD":

                # pega o valor armazenado no registrador, transforma para float, e então para int, para ser usado como chave
                endereco = reg[int(adress3, 2)]
                endereco = binary32_to_float(endereco)
                endereco = int(endereco)

                reg[int(adress1, 2)] =  mem[endereco]
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

            case "RMND":
                A, B = fetch_data(adress1, adress2)
                holder = operador.remainder(A, B)
                linha_de_comando += 1

            case "DIV_":
                A, B = fetch_data(adress1, adress2)
                holder = operador.div(A, B)
                linha_de_comando += 1

            case "POW_":
                A, B = fetch_data(adress1, adress2)
                holder = operador.power(A, B)
                linha_de_comando += 1

            case "FACT":
                A, B = fetch_data(adress1, adress2)
                holder = operador.factorial(A)
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
                print(f"({binary32_to_float(reg[int(adress1, 2)])})")
                # print(f" {reg[int(adress1, 2)]} = ({int(reg[int(adress1, 2)], 2)})")
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

            # Usado como auxilio durante testagens, para preencher linhas vazias originadas da planilha para montagem de scripts. Mantido por motivos de registro apenas
            case "FILL":
                linha_de_comando += 1
                pass

            case _:
                print(f"Invalid command: {comando}")
                linha_de_comando += 1
        
    et = time.process_time()
    print(f'Tempo de processamento da CPU {et - st}')


# força a execução da função main. Não é necessário em C
if __name__ == "__main__":
    main()
