#%%

'''
Depois de calcular a soma do valor total de vendas por combinação de unidade e categoria de produto, 
a próxima etapa é reformatar essa tabela para facilitar comparações entre unidades.

Transforme a tabela criada anteriormente para que as categorias de produto sejam as colunas, 
e cada unidade represente uma linha. Isso facilitará a visualização do desempenho de vendas 
de cada categoria por unidade.
'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

pivot_unidade_categoria = df.pivot_table(values='valor_total', 
                                         index='unidade', 
                                         columns='categoria_produto', 
                                         aggfunc='sum')

pivot_unidade_categoria
# %%
