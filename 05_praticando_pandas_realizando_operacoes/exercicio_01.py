#%%
'''
Você é um pesquisador em um instituto botânico e recebeu um conjunto de dados sobre plantas 
coletadas em diferentes regiões do país. Sua tarefa é analisar essas informações para entender 
a distribuição das plantas com base em suas alturas médias.

Os dados estão organizados em um DataFrame chamado df_plantas, com as seguintes colunas:

Especie: O nome científico da planta.
Regiao: A região onde a planta foi coletada (Norte, Sul, Leste ou Oeste).
AlturaMedia: A altura média (em metros) da planta.
Seu objetivo é dividir o DataFrame em dois subconjuntos com base na altura média das plantas:

Plantas baixas: Altura média menor ou igual a 15 metros.
Plantas altas: Altura média maior que 15 metros.
Depois de dividir os dados, calcule a soma das alturas médias para cada grupo 
(plantas baixas e plantas altas) e exiba os resultados.

Objetivo:

Divida o DataFrame em dois subconjuntos:
Um para plantas baixas (altura média menor ou igual a 15 metros).
Outro para plantas altas (altura média maior que 15 metros).
Para cada subconjunto, calcule a soma da coluna AlturaMedia.
Exiba os resultados no seguinte formato:
Grupo: Plantas Baixas
Soma das Alturas Médias: 45 m
--------------------
Grupo: Plantas Altas
Soma das Alturas Médias: 133 m
-------------------'
'''

# %%

import pandas as pd

dados = {
    'Especie': ['Mangifera indica', 'Eucalyptus globulus', 'Pinus elliottii', 'Anacardium occidentale',
                'Coffea arabica', 'Hevea brasiliensis', 'Carica papaya', 'Theobroma cacao',
                'Cocos nucifera', 'Bertholletia excelsa'],
    'Regiao': ['Norte', 'Sul', 'Leste', 'Norte', 'Sul', 'Oeste', 'Leste', 'Norte', 'Oeste', 'Norte'],
    'AlturaMedia': [15, 30, 25, 12, 3, 20, 5, 10, 18, 40]
}

df = pd.DataFrame(dados)

df['GrupoPlantas'] = df['AlturaMedia'].apply(lambda x: 'Plantas Baixas' if x <= 15 else 'Plantas Altas')

df_agrupado = df.groupby('GrupoPlantas', as_index=False)[['AlturaMedia']].sum()
df_agrupado

# %%
