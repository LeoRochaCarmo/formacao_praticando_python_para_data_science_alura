#%%

'''
Você recebeu um conjunto de dados contendo informações financeiras de várias pessoas. 
O objetivo é calcular a porcentagem de economia de cada pessoa com base em seus ganhos e despesas.

Sua tarefa é:

1 - Usar o método apply em conjunto com uma função lambda para calcular a porcentagem de economia de cada pessoa. 
A fórmula para calcular a porcentagem de economia é:
(Ganhos - Despesas) / Ganhos * 100.

2 - Criar uma nova coluna chamada Economia (%) que armazene os valores calculados.

3 - Exibir as colunas Pessoa, Ganhos, Despesas e Economia (%).

Objetivo:

Usar o método apply com uma função lambda para calcular a porcentagem de economia de cada pessoa.
Criar a nova coluna Economia (%) no DataFrame.
Exibir as colunas Pessoa, Ganhos, Despesas e Economia (%).
A saída esperada deve ser semelhante ao seguinte:

      Pessoa  Ganhos  Despesas  Economia (%)
0       Ana    5000      3000     40.000000
1     Bruno    4000      2500     37.500000
2     Carla    3500      2000     42.857143
3    Daniel    6000      5000     16.666667
4   Eduarda    2500      2000     20.000000
5    Felipe    7000      6000     14.285714
6  Gabriela    3000      2500     16.666667
7  Henrique    4500      4000     11.111111

'''

#%%

import pandas as pd

dados = {
    'Pessoa': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Ganhos': [5000, 4000, 3500, 6000, 2500, 7000, 3000, 4500],
    'Despesas': [3000, 2500, 2000, 5000, 2000, 6000, 2500, 4000]
}

df = pd.DataFrame(dados)

df['Economia (%)'] = df.apply(lambda x: (x['Ganhos'] - x['Despesas']) / x['Ganhos'] * 100, axis = 1)
df
# %%
