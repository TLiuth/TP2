from registradores import Registradores
from operacoes import Operacoes


#imprime os valores atuais dos registradores e a lista de comandos, para fins de depuração
def display(regis, comandos):
    print("REGISTRADORES:")
    for key, value in regis.items():
        print(f"[ {key} | {value} ]")
    
    print("\nCOMANDOS:")
    for chave, comando in comandos.items():
        print(f"{chave} : {comando}")


#lê os comandos do arquivo comandos.txt e os armazena em ordem num dicionário
def le_comandos(file_path):
    comandos = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove o caracter de nova linha
    lines = [line.strip() for line in lines]

    # Armazena cada linha num espaço do dicionário, com o número da linha como chave (começa em 1)
    for i, line in enumerate(lines, start=1):
        comandos[i] = line

    # retorna os comandos para um dicionário alvo
    return comandos



def main():
    regis = Registradores()

    comandos = le_comandos('comandos.txt')

    operador = Operacoes()

    sub = operador.sub('00001010', '00000001')
    print(f"Subtração {sub}")


    display(regis.reg, comandos)



if __name__ == "__main__":
    main()

