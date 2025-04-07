#%%

'''
Mariana é uma analista de marketing digital e contribui no gerenciamento de campanhas de anúncios pagos. 
Ela recebeu um conjunto de dados com informações sobre os cliques diários em anúncios de diferentes campanhas, 
custo por clique (CPC) e a categoria do anúncio.

Mariana quer entender como os cliques diários se distribuem entre as campanhas para identificar quais faixas
 de cliques são mais comuns e detectar possíveis padrões ou anomalias. 
 O que ela pode fazer para visualizar essas informações e que insights isso pode trazer?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_3.csv')

plt.figure(figsize=(10,6), dpi=400)
plt.title('Distribuição dos cliques diários', fontsize=14)
plt.ylabel('Frequência')
sn.histplot(df['Cliques Diários'], kde=True, bins=20)
sn.despine()
plt.show()

