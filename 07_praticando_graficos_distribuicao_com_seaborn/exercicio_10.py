#%%

'''
Clara é uma analista de marketing e precisa monitorar a eficácia de campanhas publicitárias em diferentes regiões do país. 
Ela tem dados sobre a idade dos usuários impactados pelas campanhas e quer analisar como a idade varia por região e se 
o usuário realizou uma compra após visualizar o anúncio.

Clara quer entender como a distribuição de idade dos usuários varia por região e como ela se relaciona com a realização 
de compras. Que gráfico seria mais adequado para analisar essa distribuição com base nas variáveis fornecidas? 
Crie o gráfico e descreva as observações.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_10.csv')

plt.figure(figsize=(8,4), dpi=400)
plt.title('Distribuição de Idade por Região e Realização de Compra)', fontsize=13)
ax =sn.violinplot(data=df, 
              x='Região', 
              y='Idade',
              hue='Compra',
              split=True,
              inner='quart')
sn.move_legend(ax, loc='upper right')
sn.despine()
plt.show()

#%%
