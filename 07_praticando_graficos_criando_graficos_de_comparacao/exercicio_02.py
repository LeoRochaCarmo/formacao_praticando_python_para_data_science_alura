#%%

'''
Nesta atividade, você dará continuidade à exploração dos dados de automóveis usados, 
focando agora na relação entre o estilo do veículo e seu valor médio de venda. 
Seu objetivo será criar um gráfico que apresente essa comparação de forma clara e 
objetiva, permitindo identificar como diferentes estilos de veículos impactam 
seus preços no mercado.

Sua tarefa será:
Agrupar os valores médios dos automóveis pela coluna que contém o estilo dos automóveis;
Ordenar o resultado do agrupamento do maior para o menor valor médio;
Escolher o tipo de gráfico mais adequado para visualizar as informações, levando em conta a quantidade de categorias;
Personalizar o gráfico para deixá-lo mais informativo e visualmente compreensível.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df_grouped = (df.groupby(by='Estilo')['Valor($)']
                .mean()
                .sort_values(ascending=False)
                .reset_index())

plt.figure(dpi=500)
plt.title('Valor médio por estilo', loc='center', fontsize = 15)
sn.barplot(x='Valor($)', y='Estilo', data=df_grouped)
sn.despine()
plt.show()


