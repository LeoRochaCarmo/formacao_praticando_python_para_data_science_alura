#%%

'''
Marcos é um analista de qualidade de sensores usados em fazendas para monitorar a produtividade semanal (em toneladas) 
de diferentes culturas agrícolas. Ele recebeu dados de produtividade para três culturas principais: Milho, Soja e Trigo.

Marcos deseja identificar outliers, analisar a variabilidade da produtividade, e entender as diferenças entre as culturas. 
O que ele pode fazer para visualizar essas informações?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_7.csv')

df.columns.tolist()

#%%
plt.figure(figsize=(8,6), dpi=400)
plt.title('Distribuições (Produtividade Semanal x Cultura)', fontsize=12)
sn.boxplot(data=df, x='Cultura', y='Produtividade Semanal (t)', hue='Cultura')
sn.despine()
plt.show()
# %%
