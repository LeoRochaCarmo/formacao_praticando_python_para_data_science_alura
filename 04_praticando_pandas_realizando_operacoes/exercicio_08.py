#%%

'''
Você recebeu um conjunto de dados que contém informações sobre o estoque de diferentes produtos 
de uma loja. O objetivo é classificar os produtos que possuem estoque abaixo de um determinado 
limite como "Estoque Baixo".

Usar o método apply com uma função lambda para criar uma nova coluna chamada Estoque Baixo, que indicará:

True (Verdadeiro) se o estoque do produto for menor que 50.
False (Falso) caso contrário.
Exibir as colunas Produto, Estoque e Estoque Baixo.

Objetivo:

Usar o método apply com uma função lambda para classificar os produtos com base na quantidade em estoque.
Criar a nova coluna Estoque Baixo no DataFrame.
Exibir as colunas Produto, Estoque e Estoque Baixo.
A saída esperada deve ser semelhante ao seguinte:

      Produto  Estoque  Estoque Baixo
0    Notebook       30           True
1       Mouse      150          False
2     Teclado       45           True
3     Monitor       20           True
4     Cadeira       60          False
5  Impressora       10           True
6   Pen Drive       80          False
7        Mesa       50          False

'''

#%%

import pandas as pd

dados = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Cadeira', 'Impressora', 'Pen Drive', 'Mesa'],
    'Estoque': [30, 150, 45, 20, 60, 10, 80, 50]
}

df = pd.DataFrame(dados)

df['EstoqueBaixo'] = df['Estoque'].apply(lambda x: True if x < 50 else False)
df

# %%
