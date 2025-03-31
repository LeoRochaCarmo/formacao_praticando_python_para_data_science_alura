#%%

'''
No mercado imobiliário, o ano de construção do imóvel pode influenciar seu valor de aluguel. 
Imóveis mais novos tendem a ter preços mais elevados devido a melhor infraestrutura, 
tecnologias modernas e menor necessidade de manutenção.

Nesta atividade, você irá analisar como o valor médio dos alugueis varia de acordo com o 
ano de construção dos imóveis, criando um gráfico que ilustre essa relação ao longo do tempo.

Sua tarefa será:
Agrupar os valores por ano de construção e calcular a média do aluguel;
Criar um gráfico adequado para visualizar essa relação ao longo do tempo;
Personalizar o gráfico para torná-lo mais informativo.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

df_grouped = df.groupby('Ano')['Valor'].mean().reset_index()

plt.figure(dpi=500)
plt.title('Valor médio aluguel por ano de construção', loc='left', fontsize=14)
sn.lineplot(x='Ano', y='Valor', data=df_grouped)
sn.despine()
plt.show()
