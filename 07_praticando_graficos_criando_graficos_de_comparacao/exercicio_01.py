#%%

'''
Nesta atividade, você terá a oportunidade de analisar um conjunto de dados sobre automóveis usados, 
explorando como o tamanho do veículo influencia seu valor médio de venda. Essa análise ajudará a 
identificar padrões ou tendências entre o tamanho dos veículos e seus preços no mercado de usados.

Sua tarefa será:
Carregar os dados;
Agrupar os valores médios dos automóveis pela coluna que contém o tamanho dos automóveis;
Ordenar o resultado do agrupamento do maior para o menor valor médio;
Escolher o tipo de gráfico mais adequado para visualizar as informações;
Personalizar o gráfico para deixá-lo mais informativo e visualmente compreensível.
'''

#%%
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df_grouped = (df.groupby('Tamanho')['Valor($)']
                 .mean()
                 .reset_index()
                 .sort_values(by='Valor($)', ascending=False))

plt.figure(dpi=500)
plt.title(label='Valor médio por tamanhos', loc='center',fontsize=15)
sn.barplot(x='Tamanho', y='Valor($)', data=df_grouped)
sn.despine()
plt.show()

# %%
