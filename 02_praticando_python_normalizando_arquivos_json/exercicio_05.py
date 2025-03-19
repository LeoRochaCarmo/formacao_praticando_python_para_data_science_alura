#%%

# Exercício 5

'''
Tiago utilizou a normalização para transformar um arquivo JSON aninhado em um DataFrame no ambiente Python. 
Contudo, ele percebeu que o separador padrão ('.') nos nomes das colunas criadas a partir dos dados aninhados 
não atende às suas necessidades.

Tiago gostaria de usar o caractere '_' como separador, resultando em nomes de colunas como: 
cliente_id_cliente, cliente_nome_cliente, compra_id_produto e compra_nome_produto. 

Como Tiago pode alterar o separador de colunas para '_' ao realizar a normalização?
'''
# %%

import pandas as pd
import json

with open ('.\\dados\\questao_5.json', 'r') as arquivo:
    dados = json.load(arquivo)

df = pd.json_normalize(dados, sep='_')
df
# %%
