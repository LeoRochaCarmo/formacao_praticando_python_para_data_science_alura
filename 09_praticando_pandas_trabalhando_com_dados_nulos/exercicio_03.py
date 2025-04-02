#%%

'''
Agora que você identificou adequadamente todos os dados nulos, você já pode seguir 
para a aplicação de um tratamento. As colunas CustomerName e CustomerRating 
são as colunas que contém dados nulos, um tratamento válido para esse conjunto é 
substituir os valores nulos do DataFrame.

Tendo isso em mente, como substituir os valores nulos da coluna CustomerName pela string 
'Não especificado' e os valores de CustomerRating pelo valor -1?
'''

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_1_2_3.csv')

df['CustomerName'] = df['CustomerName'].fillna('Não especificado')
df['CustomerRating'] = df['CustomerRating'].fillna(-1)

df

# %%

# JEITO MAIS ELEGANTE

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_1_2_3.csv')

dicionario = {'CustomerName': 'Não especificado',
              'CustomerRating': -1}

df.fillna(dicionario, inplace=True)

df

# %%
