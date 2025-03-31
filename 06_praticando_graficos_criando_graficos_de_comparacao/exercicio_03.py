#%%

'''
A qualidade do ar é um fator essencial para a saúde pública e o meio ambiente. 
Um dos principais poluentes atmosféricos é o ozônio (O₃), cuja concentração 
pode variar ao longo do tempo devido a fatores como temperatura e atividades humanas.

Nesta atividade, você irá explorar a variação diária dos níveis de ozônio em uma 
cidade localizada no continente asiático. O objetivo é criar um gráfico 
que represente essa evolução ao longo do tempo, possibilitando a identificação de 
padrões sazonais e tendências, como aumentos ou reduções na concentração desse poluente.

Sua tarefa será:
Carregar os dados;
Formatar a coluna de datas corretamente para facilitar a análise temporal;
Escolher o tipo de gráfico mais adequado para representar a evolução dos níveis de ozônio ao longo dos anos;
Personalizar o gráfico para deixá-lo mais informativo e visualmente compreensível.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/poluentes.csv'

df = pd.read_csv(url)

df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')

plt.figure(dpi=500)
plt.title('Variação diária dos níveis de ozônio', loc='left', fontsize=15)
sn.lineplot(x='Data', y='O3', data=df)
plt.xticks(rotation=-45)
sn.despine()
plt.show()

# %%
