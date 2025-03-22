#%%

'''
Nesta atividade você vai praticar como reformatar o resultado com o método unstack(), que transforma os dados 
de uma estrutura indexada por múltiplos níveis em uma forma tabular mais legível e prática para análise.

Utilize o método unstack() para transformar o índice múltiplo de região e piscina numa tabela 
onde cada região aparece como uma linha e as colunas se dividem em Piscina "Nao" e "Sim”, 
mostrando a média dos valores de aluguel. Isso facilitará a visualização direta das diferenças 
de preço entre apartamentos com e sem piscina em cada região.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

valor_piscina_regiao = df.groupby(by=['Regiao', 'Piscina'])['Valor'].mean().unstack()

valor_piscina_regiao

# %%
