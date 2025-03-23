#%%

'''
Seu desafio é incluir informações adicionais na tabela para aprimorar a análise de desempenho. 
Você deve incluir uma coluna que sumarize o valor total de vendas para cada unidade e 
adicionar uma linha ao final da tabela que mostre o total de vendas para cada categoria

Essas adições ajudarão a visualizar não apenas o desempenho individual de cada unidade, 
mas também a contribuição de cada categoria para o total de vendas, oferecendo uma 
visão compreensiva do negócio.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

df.head()

#%%

pivot_unidade_categoria = df.pivot_table(values='valor_total', 
                                         index='unidade', 
                                         columns='categoria_produto', 
                                         aggfunc='sum',
                                         margins=True,
                                         margins_name='Total')

pivot_unidade_categoria


# %%
