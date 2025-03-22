#%%
'''
Depois de avaliar o desempenho das unidades individuais da rede, a próxima tarefa é analisar o desempenho de 
vendas por categoria de produto. Esta análise é crucial para identificar quais categorias estão contribuindo 
mais significativamente para as receitas e podem ser alvos de estratégias de marketing ou ajustes de estoque.

Sua missão nesta atividade é aplicar o método groupby() para agrupar e sumarizar o valor total de vendas por 
categoria de produto. Para tornar os resultados ainda mais claros, ordene as categorias de acordo com o 
valor total de vendas, do maior para o menor.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

total_vendas_por_produto = (df.groupby(by='categoria_produto', as_index=False)[['valor_total']]
                              .sum()
                              .sort_values('valor_total', ascending=False, ignore_index=True))

total_vendas_por_produto

# %%
