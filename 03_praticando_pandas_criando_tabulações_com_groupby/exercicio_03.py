#%%

'''
Nesta atividade, vamos explorar outro dataset que contém informações sobre o preço de aluguel de apartamentos 
na cidade de São Paulo. Este conjunto de dados nos permitirá entender as variações de preços nas diferentes regiões da cidade.

Sua missão nesta atividade é aplicar o método groupby() para agrupar os dados por região e utilizar o método describe() 
para obter estatísticas descritivas do valor do aluguel. As estatísticas descritivas fornecerão insights 
importantes como média, mediana, valor mínimo, máximo e quartis, oferecendo uma visão detalhada sobre a 
distribuição dos preços de aluguel em cada região.


'''

# %%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

estatisticas_aluguel_regia0 = df.groupby(by='Regiao')['Valor'].describe()

estatisticas_aluguel_regia0

# %%
