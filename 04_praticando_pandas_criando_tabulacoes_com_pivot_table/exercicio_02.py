#%%

'''
Depois de avaliar o desempenho das unidades individuais da rede, a próxima tarefa é analisar o desempenho de 
vendas por categoria de produto. Esta análise é crucial para identificar quais categorias estão contribuindo 
mais significativamente para as receitas e podem ser alvos de estratégias de marketing ou ajustes de estoque.

Sua missão nesta atividade é aplicar o método pivot_table() para agrupar e sumarizar o valor total de vendas 
por categoria de produto. Para tornar os resultados ainda mais claros, ordene as categorias de 
acordo com o valor total de vendas, do maior para o menor.
'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_vendas_por_categoria = (df.pivot_table(values='valor_total', 
                                            index='categoria_produto', 
                                            aggfunc='sum')
                               .sort_values(by='valor_total', ascending=False)
                               )
pivot_vendas_por_categoria

# %%
