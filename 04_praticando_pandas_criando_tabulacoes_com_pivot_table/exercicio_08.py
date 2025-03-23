#%%

'''
Após investigar como o tipo de transmissão influencia o valor dos automóveis, vamos agora explorar 
como os preços variam ao longo dos anos de fabricação. Essa análise é fundamental para entender 
tendências de mercado, como a depreciação ou a valorização de automóveis com o passar do tempo, 
e pode fornecer insights valiosos para compradores e vendedores.

O objetivo desta atividade é usar o método pivot_table() para agrupar os dados com base no ano 
de fabricação dos automóveis e calcular o valor mínimo, médio e máximo dos automóveis para cada ano. 
Isso nos ajudará a entender como os valores dos carros mudaram ao longo do tempo e identificar padrões 
específicos de valorização ou depreciação.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_ano_agregacoes = df.pivot_table(values='Valor($)', index='Ano', aggfunc=['min', 'mean', 'max']).round()

pivot_ano_agregacoes

#%%

# Se livrando do MultiIndex (jeito 1)
pivot_ano_agregacoes.columns = ['valor_minimo', 'valor_medio', 'valor_maximo']

pivot_ano_agregacoes

# %%

# Se livrando do MultiIndex (jeito 2)

pivot_ano_agregacoes.columns = [col[0] + '_' + col[1].lower() for col in pivot_ano_agregacoes.columns]

pivot_ano_agregacoes

# %%
