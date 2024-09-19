from algo_genetico.algoritmo_genetico import AlgoritmoGenetico
from common.geracao_produto import GeracaoDeProdutos
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

matplotlib.use("TkAgg")

def plot_graph(melhores_cromossomos):
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
    ax.set_title('Evolução da Melhor Solução')
    ax.set_xlabel('Geração')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)

    root = tk.Tk()
    root.title("Evolução da Melhor Solução")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    button = tk.Button(master=root, text="Fechar", command=root.quit)
    button.pack(side=tk.BOTTOM)

    tk.mainloop()


def main():
    lista_produto = GeracaoDeProdutos.gerar_lista_produtos(lim=23)
    espacos = [produto.espaco for produto in lista_produto]
    valores = [produto.valor for produto in lista_produto]

    limite = 3.0
    taxa_mutacao = 0.05
    quantidade_geracoes = 1000

    algoritmo_genetico = AlgoritmoGenetico(len(lista_produto))
    resultado = algoritmo_genetico.resolver(taxa_mutacao, quantidade_geracoes, espacos, valores, limite,
                                            ate_solucao=False)

    print("****** PRODUTOS ******")
    for i, produto in enumerate(lista_produto):
        status = "OK" if resultado[i] == "1" else "NOK"
        print(f"{produto.nome} {status}")
    print("******** FIM ********")

    plot_graph(algoritmo_genetico.melhores_cromossomos)


if __name__ == "__main__":
    main()
