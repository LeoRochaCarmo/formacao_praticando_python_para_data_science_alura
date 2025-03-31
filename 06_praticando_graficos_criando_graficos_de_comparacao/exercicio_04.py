#%%

'''
Nesta atividade, você irá analisar a variação das temperaturas ao longo dos dias, criando um gráfico que ilustra essa evolução. 
Ao final, você poderá comparar este gráfico com o anterior e refletir sobre possíveis correlações entre os dois fenômenos.

Sua tarefa será:
Criar um gráfico adequado para visualizar a evolução das temperaturas ao longo do tempo;
Comparar visualmente este gráfico com o da atividade anterior e refletir sobre possíveis relações entre temperatura e ozônio;
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
plt.title('Variação da temperatura ao longo dos dias', loc='left', fontsize=18)
sn.lineplot(x='Data', y='TEMP', data=df)
sn.despine()
plt.show()