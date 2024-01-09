
#simula a memória de registradores (um dicionário com chaves de 0 a 15, inicialmente completos com bytes 0)
class Registradores():
    def __init__(self):
        self.reg = {
            0: "00000000",
            1: "00000001",
            2: "00000000",
            3: "00000000",
            4: "00000000",
            5: "00000000",
            6: "00000000",
            7: "00000000",
            8: "00000000",
            9: "00000000",
            10: "00000000",
            11: "00000000",
            12: "00000000",
            13: "00000000",
            14: "00000000",
            15: "00000000"
        }

# Simula a memória principal. 10001 espaços de memória, simulado por um dicionário com chaves de 0 a 10000, preenhcidos com bytes 0
class Memoria():
    def __init__(self):
        self.mem = {}
        for i in range(0, 10000):
            self.mem[i] = "00000000"