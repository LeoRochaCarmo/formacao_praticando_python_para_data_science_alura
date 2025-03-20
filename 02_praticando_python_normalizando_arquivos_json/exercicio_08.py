#%%

'''
Paula está trabalhando com um conjunto de dados que contém duas listas aninhadas dentro de uma chave chamada lojas. 
Devido a essa estrutura, ela está enfrentando dificuldades para transformar o documento em um DataFrame manipulável.

Ajude Paula a estruturar os dados em um DataFrame adequado para análise.
'''

import pandas as pd
import json

with open ('.\\dados\\questao_8.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

df_1 = pd.json_normalize(dados, record_path=['lojas', 'lojas_nordeste'])
df_2 = pd.json_normalize(dados, record_path=['lojas', 'lojas_norte'])

df_full = pd.concat([df_1, df_2], ignore_index=True)
df_full

# %%

