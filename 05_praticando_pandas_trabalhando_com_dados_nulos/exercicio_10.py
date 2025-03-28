#%%

'''

Você recebeu um conjunto de dados que trazem informações sobre alguns produtos vendidos na 
loja de departamentos da qual você trabalha. Ao abrir o arquivo, você percebeu que 
existem muitos dados nulos que precisam ser tratados antes desse conjunto de dados ser levado à uma análise.

A coluna Estoque tem muitos dados nulos, o que torna mais eficiente a remoção da coluna inteira ao 
invés de tentar substituir os dados ausentes. Já a coluna Categoria tem alguns dados nulos, 
então para evitar perda de mais informação, a recomendação é preencher os dados nulos com o texto 'Não especificada'.

Seu objetivo é aplicar as recomendações descritas, tratando os dados nulos desse conjunto.
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_10.csv')

df
#%%

df['Categoria'] = df['Categoria'].fillna('Não Especificado')

df.dropna(axis=1, how='any', inplace=True)

df


    