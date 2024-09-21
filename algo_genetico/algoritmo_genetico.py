import random

from algo_genetico.individuo import Individuo
from algo_genetico.exceptions import NoSuchElementException


class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.melhor_individuo = None
        self.melhores_cromossomos = []

    def inicializar_populacao(self, espacos, valores, limite_espacos):
        for _ in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))
        self.melhor_individuo = self.populacao[0]

    def encontrar_melhor_individuo(self):
        if not self.populacao:
            raise NoSuchElementException("A população está vazia.")
        return max(self.populacao, key=lambda ind: ind.nota_avaliacao)

    def avaliar_populacao(self):
        for individuo in self.populacao:
            individuo.avaliar()

    def soma_avaliacoes(self):
        return sum(ind.get_nota_avaliacao() for ind in self.populacao)

    def melhor_individuo_das_populacoes(self):
        melhor_individuo_atual = self.encontrar_melhor_individuo()
        if melhor_individuo_atual.nota_avaliacao > self.melhor_individuo.nota_avaliacao:
            self.melhor_individuo = melhor_individuo_atual

    def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite, ate_solucao=False):
        self.inicializar_populacao(espacos, valores, limite)
        self.avaliar_populacao()
        self.melhor_individuo_das_populacoes()

        while True:
            for geracao in range(1 if ate_solucao else numero_geracoes):
                soma_avaliacao = self.soma_avaliacoes()
                nova_populacao = []

                for _ in range(0, self.tamanho_populacao, 2):
                    pai1 = self.selecionar_pai(soma_avaliacao)
                    pai2 = self.selecionar_pai(soma_avaliacao)

                    filhos = pai1.crossover(pai2)
                    nova_populacao.extend(filhos)

                for individuo in nova_populacao:
                    individuo.mutacao(taxa_mutacao)
                    individuo.avaliar()

                self.populacao = nova_populacao
                self.avaliar_populacao()
                self.encontrar_melhor_individuo()
                self.melhor_individuo_das_populacoes()
                self.visualizar_geracao()

                self.visualizar_melhor_solucao()
            if not ate_solucao:
                break

        return self.melhor_individuo.cromossomo

    def selecionar_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random.random() * soma_avaliacao
        soma = 0.0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].get_nota_avaliacao()
            pai += 1
            i += 1
        return self.populacao[pai]

    def visualizar_geracao(self):
        melhor_individuo_atual = self.encontrar_melhor_individuo()
        print(f"G: {melhor_individuo_atual.geracao} "
              f"Valor: {melhor_individuo_atual.nota_avaliacao} "
              f"Espaço: {melhor_individuo_atual.espaco_usado} "
              f"Cromossomo: {''.join(melhor_individuo_atual.cromossomo)}")
        self.melhores_cromossomos.append(melhor_individuo_atual)

    def visualizar_melhor_solucao(self):
        print(f"Melhor solucao G -> {self.melhor_individuo.geracao} "
              f"Valor: {self.melhor_individuo.nota_avaliacao} "
              f"Espaço: {self.melhor_individuo.espaco_usado} "
              f"Cromossomo: {''.join(self.melhor_individuo.cromossomo)}")