#%%

# Exercício 6

'''
Cristina recebeu um arquivo JSON com dados importantes para sua avaliação de lojas. 
Contudo, ao aplicar a função json_normalize, o resultado obtido não foi um DataFrame normalizado 
e organizado como esperado:

Ajude Cristina a criar um DataFrame que permita a manipulação adequada de todos os dados.
'''

# %%

import pandas as pd
import json

with open ('.\\dados\\questao_6.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

df = pd.json_normalize(dados, sep='_', record_path='lista_lojas')
df



# %%


