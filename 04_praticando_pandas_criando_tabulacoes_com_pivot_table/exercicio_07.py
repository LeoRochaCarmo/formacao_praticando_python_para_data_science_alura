#%%

'''
Continuando nossa análise do mercado de automóveis usados, vamos agora explorar como o tipo de transmissão 
pode afetar o valor de revenda dos automóveis.

O objetivo desta atividade é usar o método pivot_table() para agrupar os dados com base no tipo de 
transmissão e calcular o valor médio dos automóveis para cada tipo de transmissão. 
Isso nos ajudará a entender se há uma diferença significativa no valor médio dos carros 
dependendo se eles são automáticos, manuais ou de outro tipo.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_transmissao = (df.pivot_table(values='Valor($)', index='Tipo_transmissao')
                       .round()
                       .sort_values('Valor($)', ascending=False))

pivot_transmissao

# %%
