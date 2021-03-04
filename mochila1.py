from operator import attrgetter

class Objeto:
    def __init__(self, id, p, u):
        self.id = id;
        self.peso = p;
        self.utilidade = u;
        self.profit = u/p;
    def __repr__(self):
        return str(f"id={self.id}:p={self.peso}:u={self.utilidade}:pf={self.profit}")

class Mochila:
    def __init__(self):
        self.capacidade_max = 10;
        self.objetos = []

    def calcula_fo(self):
        self.pesos= 0;
        self.utilidades= 0;
        self.penalidades= 0;
        for item in self.objetos:
            self.pesos += item.peso;
            self.utilidades += item.utilidade;
            self.penalidades += item.peso;
        self.fo = self.utilidades - self.penalidades * max(0, self.pesos - self.capacidade_max)

    def imprimir_solucao(self):
        self.calcula_fo()
        print(f"FO:{self.fo}\nPeso:{self.pesos}\nUtilidade:{self.utilidades}")


numero_objetos = 3
arquivo_pesos = [3, 1, 1]
arquivo_capacidades = [3, 2, 1]
arquivo_utilidades = [3, 2, 1]
mochila = Mochila()

#montar mobjetos
objetos = []
for i in range(numero_objetos):
    objetos.append(Objeto(i, arquivo_pesos[i], arquivo_utilidades[i]))
print(objetos)
s = sorted(objetos, key=attrgetter('profit'), reverse=True)
print(s)
mochila.imprimir_solucao()
