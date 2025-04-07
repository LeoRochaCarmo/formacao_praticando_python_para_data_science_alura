#%%

'''
Joana é uma gestora de logística e está avaliando o tempo de entrega dos pedidos realizados pelos clientes. 
Ela recebeu um conjunto de dados com os tempos de entrega registrados na última semana e deseja entender 
visualizar esses dados. O objetivo é identificar a mediana, a variabilidade, e possíveis outliers que 
representem atrasos significativos ou entregas extremamente rápidas.

Joana quer visualizar a distribuição dos tempos de entrega para cumprir seus objetivos. 
O que ela pode fazer para visualizar essas informações?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_6.csv')

plt.figure(figsize=(8,4), dpi=400)
plt.title('Distribuição dos tempos de entrega', fontsize=12)
sn.boxplot(x='Tempo de Entrega (horas)', data=df)
sn.despine()
plt.show()

