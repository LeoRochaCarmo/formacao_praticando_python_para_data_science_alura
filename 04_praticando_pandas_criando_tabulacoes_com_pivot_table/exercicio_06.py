#%%

'''
Nesta atividade, vamos investigar um outro conjunto de dados que contém informações sobre automóveis usados. 
Esses dados incluem detalhes como o estilo do carro, o ano de fabricação, a quilometragem, entre outros 
aspectos relevantes.

O desafio proposto aqui é utilizar o método pivot_table() para agrupar os dados com base no estilo do 
automóvel e calcular o valor médio dos carros para cada estilo, organizando os resultados em ordem 
decrescente de valor. Essa análise permitirá identificar quais estilos de automóveis mantêm maior 
valor de mercado e podem ser mais atrativos para revendedores e compradores.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_estilo = df.pivot_table(values='Valor($)', index='Estilo').sort_values('Valor($)', ascending=False).round()
pivot_estilo

# %%
