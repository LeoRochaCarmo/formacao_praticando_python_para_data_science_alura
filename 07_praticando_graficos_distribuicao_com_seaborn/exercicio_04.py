#%%

'''
Ana é uma analista de dados em uma empresa especializada no monitoramento de dados de saúde. 
Ela recebeu um conjunto de dados que contém a pressão arterial sistólica (medida em mmHg) de 500 pacientes.

Ana quer entender a distribuição das medidas de pressão arterial sistólica dos pacientes. 
O que ela pode fazer para visualizar essas informações e identificar se há uma concentração em intervalos específicos?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_4.csv')

plt.figure(figsize=(8,4), dpi=400)
plt.title('Distribuição das medidas de pressão sistólica', fontsize=14)
plt.ylabel('Densidade', fontsize=10)
plt.xlabel('Pressão Sistólica (mmHg)', fontsize=10)
sn.kdeplot(df['Pressão Sistólica (mmHg)'], fill=True, alpha=0.6)
sn.despine()
plt.show()
