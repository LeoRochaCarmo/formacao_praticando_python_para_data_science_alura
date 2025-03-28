#%%

'''
Augusto recebeu um conjunto de dados de alguns clientes cadastrados na empresa em que ele trabalha. 
Ele percebeu que algumas colunas têm vários campos ausentes, o que as tornam inadequadas para análises.

Augusto sabe que as colunas possuem muitos valores ausentes, portanto, para facilitar sua análise, 
é mais eficiente excluí-las evitando inconsistências. Como Augusto poderia remover as colunas com 
dados ausentes no conjunto de dados?
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_7.csv')

df.dropna(axis=1, inplace=True)

df
