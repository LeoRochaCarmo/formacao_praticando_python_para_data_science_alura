#%%

# Exercício 7

'''
Juan recebeu um conjunto de dados em formato JSON e precisa normalizá-lo para acessar as informações de 
maneira estruturada. No entanto, ao utilizar json_normalize, ele identificou que o arquivo continha 
duas listas.

Como Juan pode estruturar esses dados em um único DataFrame?
'''

# %%

import pandas as pd
import json

with open ('.\\dados\\questao_7.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# normalizando os dataframes separadamente
df_1 = pd.json_normalize(dados, record_path=['lojas_sudeste'])
df_2 = pd.json_normalize(dados, record_path=['lojas_sul'])

# concatenando os dois dataframes
df_final = pd.concat([df_1, df_2], ignore_index=True)
df_final

# %%


