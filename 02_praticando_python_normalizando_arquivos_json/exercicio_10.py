#%%

'''
Agora que você explorou diversas formas de trabalhar com dicionários utilizando a 
função json_normalize e aprendeu a identificar as características de arquivos JSON 
para aplicar a normalização adequada, crie um código que permita construir 
um DataFrame manipulável a partir dos dados estruturados abaixo:
'''

dados = [
    {
        "id_loja": 17,
        "nome_loja": "Loja Rho",
        "detalhes": [
            {"cidade": "João Pessoa", "estado": "PB"}
        ],
        "vendas": [
            {"categoria": "Roupas", "vendas_mensais": 125, "faturamento_mensal": 37500.0}
        ]
    },
    {
        "id_loja": 18,
        "nome_loja": "Loja Sigma",
        "detalhes": [
            {"cidade": "Vitória", "estado": "ES"}
        ],
        "vendas": [
            {"categoria": "Calçados", "vendas_mensais": 180, "faturamento_mensal": 54000.0}
        ]
    },
    {
        "id_loja": 19,
        "nome_loja": "Loja Tau",
        "detalhes": [
            {"cidade": "Aracaju", "estado": "SE"}
        ],
        "vendas": [
            {"categoria": "Acessórios", "vendas_mensais": 90, "faturamento_mensal": 27000.0}
        ]
    },
    {
        "id_loja": 20,
        "nome_loja": "Loja Upsilon",
        "detalhes": [
            {"cidade": "Teresina", "estado": "PI"}
        ],
        "vendas": [
            {"categoria": "Livros", "vendas_mensais": 240, "faturamento_mensal": 72000.0}
        ]
    }
]
# %%

import pandas as pd
import json

df_detalhes = pd.json_normalize(dados, record_path=['detalhes'], meta=['id_loja', 'nome_loja'])
df_vendas = pd.json_normalize(dados, record_path=['vendas'], meta=['id_loja', 'nome_loja'])

df = df_detalhes.merge(df_vendas, how='left', on=['id_loja' ,'nome_loja'])
df

# %%
