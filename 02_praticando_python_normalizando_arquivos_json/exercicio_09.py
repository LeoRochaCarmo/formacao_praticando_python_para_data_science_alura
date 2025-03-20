#%%

'''
Após aplicar a normalização em uma lista presente no banco de dados, Diego percebeu que algumas colunas 
estavam ausentes no DataFrame resultante, embora estivessem nos dados originais. Ele sabe que o conjunto de 
dados deveria conter as seguintes colunas:

['cidade', 'estado', 'categoria', 'vendas_mensais', 'faturamento_mensal', 'id_loja', 'nome_loja']

No entanto, após aplicar a função json_normalize, as colunas 'id_loja' e 'nome_loja' não foram incluídas no DataFrame.

O que Diego pode ter esquecido de fazer ao configurar o código de normalização? Qual seria a forma ideal de resolver esse problema?
'''

import pandas as pd
import json

with open ('.\\dados\\questao_9.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# meta -> indica quais colunas de nível superior devem ser incluídas
df = pd.json_normalize(dados, record_path='vendas', meta=['id_loja', 'nome_loja'])
df
# %%