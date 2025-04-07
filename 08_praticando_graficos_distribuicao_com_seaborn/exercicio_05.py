#%%

'''
João é um analista de desempenho em uma empresa que oferece cursos online em diversas áreas. 
Ele recebeu um conjunto de dados sobre a nota final obtida pelos alunos em três cursos diferentes: 
Python Básico, Análise de Dados, e Machine Learning.

João quer analisar como a distribuição das notas varia entre os cursos, para entender se algum 
deles apresenta padrões diferenciados, como notas mais altas ou mais baixas. 
O que ele pode fazer para visualizar essas distribuições de forma clara?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_5.csv')
plt.figure(figsize=(8,4), dpi=400)
plt.title('Distribuição Notas x Curso', fontsize=12)
plt.ylabel('Densidade', fontsize=10)
plt.xlabel('Notal Final', fontsize=10)
ax = sn.kdeplot(x='Nota Final', 
           data=df, 
           fill=True, 
           alpha=0.5, 
           hue='Curso',
           common_norm=False)
sn.despine()
sn.move_legend(ax, 'upper left')
plt.show()