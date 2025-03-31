#%%

'''
O mercado de videogames é um dos mais lucrativos da indústria do entretenimento. 
Diferentes gêneros de jogos apresentam desempenhos variados em vendas globais, 
dependendo de fatores como popularidade, público-alvo e tendências do mercado.

Nesta atividade, você analisará o total de vendas globais para cada gênero de jogo, 
criando um gráfico que ilustre quais gêneros geraram mais receita.

Sua tarefa será:
Carregar os dados;
Agrupar os valores de vendas globais por gênero;
Ordenar os valores do maior para o menor;
Criar um gráfico adequado para visualizar essa comparação;
Personalizar o gráfico para torná-lo mais informativo e visualmente compreensível.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_jogos.csv'

df = pd.read_csv(url)

df_grouped = (df.groupby('genero')['vendas_globais']
                .count()
                .sort_values(ascending=False)
                .reset_index())

# fig, ax = plt.subplots()
# bar_container = ax.bar(x='vendas_globais', y='genero')
# plt.figure(dpi=500)
# plt.title('Total vendas globais por gênero', loc='left', fontsize=15)
# sn.barplot(x='vendas_globais', y='genero', data=df_grouped, hue='genero')
# plt.xlabel('')
# plt.ylabel('')
# plt.bar_label(df_grouped, label_type='edge')
# sn.despine()
# plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Criando a figura e os eixos
fig, ax = plt.subplots(dpi=500)

# Criando o gráfico de barras com Seaborn
barplot = sns.barplot(x='vendas_globais', y='genero', data=df_grouped, hue='genero')

# Adicionando rótulos nas barras
for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=4.5)

# Configurações adicionais
ax.set_title('Total vendas globais por gênero', loc='left', fontsize=15)
ax.set_xlabel('')
ax.set_ylabel('')
sns.despine()

# Exibir o gráfico
plt.show()


