import random

class Individuo:
    def __init__(self, espacos, valores, limite_espacos):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0.0
        self.espaco_usado = 0.0
        self.geracao = 0
        self.cromossomo = [str(random.randint(0, 1)) for _ in espacos]

    def avaliar(self):
        nota = 0.0
        soma_espacos = 0.0

        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == "1":
                nota += self.valores[i]
                soma_espacos += self.espacos[i]

        if soma_espacos > self.limite_espacos:
            nota = 1.0

        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos

    def crossover(self, outro_individuo):
        corte = round(random.random() * len(self.cromossomo))

        filho1 = outro_individuo.cromossomo[:corte] + self.cromossomo[corte:]
        filho2 = self.cromossomo[:corte] + outro_individuo.cromossomo[corte:]

        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos),
                  Individuo(self.espacos, self.valores, self.limite_espacos)]

        filhos[0].cromossomo = filho1
        filhos[0].geracao = self.geracao + 1

        filhos[1].cromossomo = filho2
        filhos[1].geracao = self.geracao + 1

        return filhos

    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random.random() < taxa_mutacao:
                self.cromossomo[i] = "0" if self.cromossomo[i] == "1" else "1"

    def get_nota_avaliacao(self):
        return self.nota_avaliacao

    def get_espaco_usado(self):
        return self.espaco_usado

    def get_geracao(self):
        return self.geracao