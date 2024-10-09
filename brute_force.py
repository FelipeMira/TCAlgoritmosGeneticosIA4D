from common.geracao_produto import GeracaoDeProdutos
from itertools import combinations
import matplotlib.pyplot as plt
import math
import time

def plot_graph(melhores_cromossomos, execution_time):
    geracoes = list(range(len(melhores_cromossomos)))
    valores = [sum([prod.valor for prod in melhor]) for melhor in melhores_cromossomos]
    volumes = [sum([prod.espaco for prod in melhor]) for melhor in melhores_cromossomos]

    best_index = valores.index(max(valores))
    best_value = valores[best_index]
    best_volume = volumes[best_index]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(geracoes, valores, marker='o', linestyle='-', color='b', label='Melhores soluções')
    ax.plot(best_index, best_value, marker='o', color='r', label=f'Melhor valor: {best_value}, Volume: {best_volume}')
    ax.set_title(f'Evolução da Melhor Solução (Brute Force)\nTempo de Execução: {execution_time:.2f} segundos')
    ax.set_xlabel('Geração (Chunk de Combinações)')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)

    plt.show()


def brute_force_knapsack(produtos, limite, chunk_size=100):
    """
    A função brute_force_knapsack resolve o problema de knapsack utilizando força bruta.
    Ela gera todas as combinações possíveis de produtos e avalia quais podem ser
    colocadas na mochila sem ultrapassar o limite de espaço, maximizando o valor total.
    
    As combinações são divididas em "chunks" (pedaços) para simular gerações, 
    e após cada avaliação de chunk, a melhor solução até aquele ponto é armazenada.
    Isso permite a visualização da evolução das melhores soluções de forma semelhante
    a um algoritmo genético.
    """
    melhor_solucao = []
    melhor_valor = 0
    melhores_cromossomos = []

    total_combinacoes = 2 ** len(produtos)  # Número total de combinações
    num_chunks = math.ceil(total_combinacoes / chunk_size)  # Número de pseudo-gerações
    todas_combinacoes = []

    # Gera todas as combinações possíveis e divide em pedaços
    for r in range(1, len(produtos) + 1):
        todas_combinacoes.extend(combinations(produtos, r))

    # Avalia as combinações em pedaços (chunks)
    for chunk_index in range(num_chunks):
        start_index = chunk_index * chunk_size
        end_index = min(start_index + chunk_size, len(todas_combinacoes))

        for combo in todas_combinacoes[start_index:end_index]:
            espaco_total = sum(produto.espaco for produto in combo)
            valor_total = sum(produto.valor for produto in combo)

            if espaco_total <= limite and valor_total > melhor_valor:
                melhor_solucao = combo
                melhor_valor = valor_total

        # Após avaliar o chunk atual, adiciona a melhor solução à lista de acompanhamento
        melhores_cromossomos.append(list(melhor_solucao))

    return melhores_cromossomos


def main():
    lista_produto = GeracaoDeProdutos.gerar_lista_produtos(lim=23)
    limite = 3.0
    chunk_size = 1000  # Simula gerações dividindo a busca de força bruta

    start_time = time.time()
    melhores_cromossomos = brute_force_knapsack(lista_produto, limite, chunk_size)
    end_time = time.time()
    execution_time = end_time - start_time

    print("****** MELHOR SOLUÇÃO ******")
    melhor_solucao = melhores_cromossomos[-1]
    for produto in melhor_solucao:
        print(f"{produto.nome} OK")
    print("******** FIM ********")

    # Plota a evolução da melhor solução
    plot_graph(melhores_cromossomos, execution_time)


if __name__ == "__main__":
    main()
