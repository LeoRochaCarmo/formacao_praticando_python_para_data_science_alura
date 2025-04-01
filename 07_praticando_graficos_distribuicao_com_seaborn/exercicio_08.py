#%%

'''
Renato é um analista ambiental e está fazendo o monitoramento da concentração de dióxido de carbono (CO2) 
em uma floresta ao longo de um ano. Ele coletou dados diários da concentração de CO2 (em ppm - partes por milhão) 
e quer entender como esses valores estão distribuídos junto aos valores de quantis.

Renato quer visualizar a distribuição geral da concentração de CO2 na floresta ao longo do ano. 
O que ele pode fazer para entender melhor os padrões gerais desses dados?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_8.csv')

plt.title('Concentração de CO2 ao longo do ano', fontsize=14)
plt.xlabel('Densidade')
sn.violinplot(data=df, y='Concentração de CO2 (ppm)', inner='quart')
sn.despine()
plt.show()