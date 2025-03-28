#%%

'''
Isadora está avaliando dados relacionados à visitas em um Parque Turístico 
ao longo de 10 dias para avaliar a eficiência das ações de marketing executadas. 
Ao verificar os dados, ela percebeu que faltavam alguns valores no registro.

Isadora acompanhou todos os dias de visitas ao parque e coleta de dados, ela 
sabe que a quantidade de visitantes variava suavemente entre os dias consecutivos. 
Portanto, ela entendeu que a forma ideal de garantir uma continuidade linear nos 
dados é substituindo os valores ausentes por meio de uma técnica de interpolação linear.

Como Isadora poderia realizar essa substituição?

Como uma extensão da atividade, realize a plotagem do número de visitantes 
por dia no Parque Turístico que Isadora trabalha.

'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividades_6.csv')

df['Visitantes'] = df['Visitantes'].interpolate()

plt.figure(dpi=500)
graph = sn.barplot(df, x= 'Data', y= 'Visitantes')
plt.xticks(rotation=-45)
plt.show()

