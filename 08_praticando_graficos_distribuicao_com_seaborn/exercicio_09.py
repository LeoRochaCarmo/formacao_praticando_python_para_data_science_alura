#%%

'''
Paulo é um analista de recursos humanos e está monitorando a carga horária semanal de trabalho (em horas) 
dos colaboradores em diferentes setores: TI, Vendas, e Financeiro. Ele deseja entender como as horas de 
trabalho estão distribuídas em cada setor, incluindo faixas de maior concentração, 
simetria ou assimetria, e diferenças gerais entre os setores.

Paulo quer entender como as horas de trabalho semanais estão distribuídas entre os setores e 
identificar padrões gerais de concentração ou dispersão. 
O que ele pode fazer para visualizar essas distribuições?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_9.csv')

df.shape

plt.figure(figsize=(8,5), dpi=400)
plt.title('Distribuições (Horas de trabalho semanais x Setor)', fontsize=12)
sn.violinplot(data=df, 
              x='Setor', 
              y='Horas de Trabalho Semanais', 
              hue='Setor',
              inner='quart')
sn.despine()
plt.show()
