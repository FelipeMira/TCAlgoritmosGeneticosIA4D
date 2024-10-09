from algo_genetico.algoritmo_genetico import AlgoritmoGenetico
from common.geracao_produto import GeracaoDeProdutos
import matplotlib.pyplot as plt
import time

def plot_graph(melhores_cromossomos, execution_time):
    geracoes = list(range(len(melhores_cromossomos)))
    valores = [ind.get_nota_avaliacao() for ind in melhores_cromossomos]
    volumes = [ind.get_espaco_usado() for ind in melhores_cromossomos]
    geracoes_ = [ind.get_geracao() for ind in melhores_cromossomos]

    best_index = valores.index(max(valores))
    best_value = valores[best_index]
    best_volume = volumes[best_index]
    best_geracao = geracoes_[best_index]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(geracoes, valores, marker='o', linestyle='-', color='b', label='Melhores soluções')
    ax.plot(best_index, best_value, marker='o', color='r', label=f'Valor da melhor solução: {best_value}, Volume: {best_volume}, Geração: {best_geracao}')
    ax.set_title(f'Evolução da Melhor Solução\nTempo de Execução: {execution_time:.2f} segundos')
    ax.set_xlabel('Geração')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)

    plt.show()

def main():
    lista_produto = GeracaoDeProdutos.gerar_lista_produtos(lim=23)
    espacos = [produto.espaco for produto in lista_produto]
    valores = [produto.valor for produto in lista_produto]

    limite = 3.0
    taxa_mutacao = 0.05
    quantidade_geracoes = 3000

    algoritmo_genetico = AlgoritmoGenetico(len(lista_produto))

    start_time = time.time()
    resultado = algoritmo_genetico.resolver(taxa_mutacao, quantidade_geracoes, espacos, valores, limite, ate_solucao=False)
    end_time = time.time()
    execution_time = end_time - start_time

    print("****** PRODUTOS ******")
    for i, produto in enumerate(lista_produto):
        status = "OK" if resultado[i] == "1" else "NOK"
        print(f"{produto.nome} {status}")
    print("******** FIM ********")

    plot_graph(algoritmo_genetico.melhores_cromossomos, execution_time)


if __name__ == "__main__":
    main()
