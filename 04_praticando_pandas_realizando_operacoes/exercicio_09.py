#%%

'''
Você recebeu um conjunto de dados com informações sobre as vendas realizadas por diferentes 
vendedores em uma loja. O objetivo é criar uma análise personalizada para calcular o 
desempenho de cada vendedor com base em suas metas, vendas realizadas e comissões.

Sua tarefa é:

1 - Usar o método apply para criar uma nova coluna chamada Desempenho, que indica o desempenho 
do vendedor com base nas vendas realizadas:
Se as vendas forem maiores ou iguais à meta, o desempenho deve ser "Atingiu a Meta".
Se as vendas forem menores que a meta, o desempenho deve ser "Não Atingiu a Meta".

2 - Usar o método apply para calcular o valor total da comissão de cada vendedor e 
armazená-lo em uma nova coluna chamada Comissão Recebida. O cálculo deve ser feito com a fórmula:

Fórmula para calcular a comissão recebida: Comissão Recebida = (Comissão (%) / 100) x Vendas.

3 - Exibir as colunas Vendedor, Meta, Vendas, Desempenho e Comissão Recebida.

Objetivo:

Criar a nova coluna Desempenho com base na comparação entre as colunas Vendas e Meta.
Criar a nova coluna Comissão Recebida com base no cálculo da comissão.
Exibir as colunas Vendedor, Meta, Vendas, Desempenho e Comissão Recebida.
A saída esperada deve ser semelhante ao seguinte:

    Vendedor    Meta  Vendas        Desempenho  Comissão Recebida
0       Ana  20000   22000   Atingiu a Meta          1100.00
1     Bruno  15000   14000  Não Atingiu a Meta         560.00
2     Carla  18000   19000   Atingiu a Meta          1140.00
3    Daniel  25000   24000  Não Atingiu a Meta        1200.00
4   Eduarda  12000   13000   Atingiu a Meta           520.00
5    Felipe  30000   28000  Não Atingiu a Meta       1960.00
6  Gabriela  10000    9000  Não Atingiu a Meta        270.00
7  Henrique  22000   23000   Atingiu a Meta          1380.00

'''

#%%

import pandas as pd

dados = {
    'Vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Meta': [20000, 15000, 18000, 25000, 12000, 30000, 10000, 22000],
    'Vendas': [22000, 14000, 19000, 24000, 13000, 28000, 9000, 23000],
    'Comissão (%)': [5, 4, 6, 5, 4, 7, 3, 6]
}

df = pd.DataFrame(dados)

df['Desempenho'] = df.apply(lambda x: 'Atingiu a meta' if x['Vendas'] >= x['Meta'] else 'Não atingiu a meta', axis=1)
df['Comissão Recebida'] = (df['Comissão (%)'] / 100) * df['Vendas']

df_view = df.drop(columns='Comissão (%)')
df_view

# %%
