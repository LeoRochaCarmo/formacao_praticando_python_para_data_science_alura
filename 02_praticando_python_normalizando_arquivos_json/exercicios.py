#%%

import pandas as pd
import json

#%%

# Exercício 01

'''
João possui um arquivo JSON contendo dados sobre as vendas da loja onde trabalha, salvo em sua máquina. 
Ele deseja processar esse arquivo no Python utilizando a biblioteca Pandas.
Ajude João a criar um código que carregue o arquivo JSON como um DataFrame.
'''

df_01 = pd.read_json('.\\dados\\questao_1.json')
df_01

# %%

# Exercício 02

'''
Márcia recebeu dois conjuntos de dados em formato JSON. O primeiro conjunto contém informações referentes 
à primeira semana do mês na loja onde trabalha, e o segundo conjunto refere-se à segunda semana.

Márcia deseja saber a forma mais eficiente de carregar esses dados no Python para manipulá-los como DataFrames. 
Analise os conjuntos e indique a melhor abordagem para resolver o problema.
'''

df_02 = pd.read_json('.\\dados\\questao_2_1.json')
df_03 = pd.read_json('.\\dados\\questao_2_2.json')

df_03

# %%

# Exercício 03

'''
Thais utilizou a função pd.read_json para carregar um arquivo JSON recebido em sua empresa. 
No entanto, ela notou que não conseguia acessar corretamente todos os dados do arquivo no DataFrame.

Um problema identificado foi que a coluna detalhes_compra apresentava informações importantes em 
formato de dicionário, dificultando a manipulação dos dados.

Ajude Thais a acessar todas as colunas e informações disponíveis nos dados.

'''

with open ('.\\dados\\questao_3.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

dados
    
df_04 = pd.json_normalize(dados, sep='_')
df_04

# %%

# E