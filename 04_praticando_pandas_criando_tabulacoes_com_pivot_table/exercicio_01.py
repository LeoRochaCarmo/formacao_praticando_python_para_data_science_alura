#%%

'''
Nesta atividade, você está trabalhando com dados de uma rede de lojas de departamentos e precisa explorar as 
características demográficas dos clientes para entender melhor seus hábitos de compra. 
Uma das perguntas chave para a análise demográfica é identificar a idade média dos clientes de acordo com o método de pagamento utilizado.

Sua tarefa é carregar os dados de vendas, explorar as informações disponíveis, e aplicar o método pivot_table() 
para calcular a média de idade dos clientes por método de pagamento.
'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_idade_media = (df.pivot_table(values='idade', index='metodo_pagamento')
                       .round()
                       .rename(columns={'idade': 'media_idade'}))

pivot_idade_media

# %%
