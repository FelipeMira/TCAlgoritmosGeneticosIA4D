# Algoritmo Genético para Otimização

## Descrição do Projeto

Este projeto implementa um algoritmo genético para resolver problemas de otimização. O algoritmo é aplicado a um conjunto de produtos, onde cada produto tem um valor e um espaço ocupado. O objetivo é encontrar a melhor combinação de produtos que maximize o valor total sem exceder um limite de espaço.

## Estrutura do Projeto

- `algo_genetico/algoritmo_genetico.py`: Contém a implementação do algoritmo genético.
- `algo_genetico/individuo.py`: Define a classe `Individuo`, que representa uma solução candidata.
- `common/geracao_produto.py`: Gera a lista de produtos a serem utilizados no algoritmo.
- `genetico.py`: Script principal que executa o algoritmo genético e plota os resultados.
- `brute_force.py`: Script executa o brute force para comparação com o genético.

## Funcionamento do Algoritmo

### 1. Inicialização

O algoritmo começa gerando uma população inicial de indivíduos. Cada indivíduo é uma combinação aleatória de produtos.

### 2. Avaliação

Cada indivíduo é avaliado com base no valor total dos produtos selecionados e no espaço total ocupado. Se o espaço ocupado exceder o limite, a avaliação do indivíduo é penalizada.

```python
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
```

*Funcionamento*
- A função avaliar calcula a avaliação de um indivíduo somando os valores dos genes ativos ("1") e os espaços correspondentes.
- Se o espaço total usado exceder o limite permitido, a avaliação é penalizada.
- Os resultados são armazenados nas variáveis de instância self.nota_avaliacao e self.espaco_usado.


### 3. Seleção

Os indivíduos são selecionados para reprodução com base em suas avaliações. Indivíduos com avaliações melhores têm maior probabilidade de serem selecionados, pois estamos utilizando a roleta ponderada, onde a probabilidade do indivíduo ser selecionado é proporcional a sua avaliação.

```python
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
```

*Funcionamento*
- Valor Sorteado: Um valor aleatório é sorteado entre 0 e a soma das avaliações. Este valor determina o ponto de corte na roleta.
- Acumulação de Avaliações: As avaliações dos indivíduos são acumuladas até que a soma ultrapasse o valor sorteado.
- Seleção do Indivíduo: O indivíduo correspondente ao ponto onde a soma ultrapassa o valor sorteado é selecionado.

Este método garante que indivíduos com avaliações mais altas têm uma maior probabilidade de serem selecionados, pois contribuem mais para a soma acumulada.

### 4. Crossover

Os indivíduos selecionados são cruzados para gerar novos indivíduos (filhos). O crossover combina partes dos cromossomos dos pais para criar os cromossomos dos filhos.

```python
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
```

*Funcionamento*
- O crossover combina a informação genética de dois pais para gerar novos indivíduos.
- Um ponto de corte é escolhido aleatoriamente e os cromossomos dos pais são recombinados para formar os filhos.
- Este processo é essencial para introduzir variabilidade genética na população e explorar novas soluções no espaço de busca.

### 5. Mutação

Os cromossomos dos filhos podem sofrer mutações aleatórias, onde alguns genes são alterados. Isso introduz variabilidade na população.

```python
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random.random() < taxa_mutacao:
                self.cromossomo[i] = "0" if self.cromossomo[i] == "1" else "1"
```

*Funcionamento*
- A função mutacao percorre cada gene do cromossomo.
- Com uma probabilidade definida pela taxa_mutacao, cada gene pode ser invertido.
- Este processo introduz variações nos indivíduos, ajudando a explorar novas soluções no espaço de busca.

### 6. Nova Geração

Os filhos gerados substituem a população atual, e o processo é repetido por um número definido de gerações.

*Funcionamento*
- Isso é feito na linha 57 na classe `algoritmo_genetico.py`, no método `resolver`, onde a nova população é atribuída à população atual.

### 7. Visualização

Ao final do processo, os resultados são plotados usando `matplotlib` e exibidos em uma janela Tkinter.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
    ```sh
    pip install matplotlib
    ```

    ou

    ```sh
    pip install -r requirements.txt
    ```
3. Execute o script `genetico.py`:
    ```sh
    python genetico.py
    ```

Caso queira executar o brute force, rode:
```sh
python brute_force.py
```

## Conclusão

Este projeto demonstra a aplicação de um algoritmo genético para resolver problemas de otimização. Através de seleção, crossover e mutação, o algoritmo busca encontrar a melhor combinação de produtos que maximize o valor total sem exceder o limite de espaço.

## Troubleshooting 


### Problema com tkinter

```
import _tkinter # If this fails your Python may not be configured for Tk
```

Em alguns casos o Python instalado não possui o Tkinter. Você pode acompanhar esse postb para possíveis resoluções.
https://stackoverflow.com/questions/5459444/tkinter-python-may-not-be-configured-for-tk