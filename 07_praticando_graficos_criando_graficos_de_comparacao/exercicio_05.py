#%%

'''
O mercado imobiliário de São Paulo é dinâmico e os preços dos alugueis podem variar de acordo com a região da cidade. 
Entender essas variações é fundamental para quem deseja alugar um imóvel ou investir no setor imobiliário.

Nesta atividade, você irá analisar o preço médio dos alugueis de alguns apartamentos em São Paulo por região, 
criando um gráfico que compara essas médias de forma visual e intuitiva.

Sua tarefa será:
Carregar os dados;
Agrupar os valores por região e calcular a média do aluguel;
Ordenar os valores do maior para o menor;
Criar um gráfico adequado para comparar os preços entre as regiões;
Personalizar o gráfico e usar cores diferentes para cada região. Se surgir alguma dúvida, consulte a opinião da pessoa instrutora!
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

df_grouped = (df.groupby('Regiao')['Valor']
                .mean()
                .sort_values(ascending=False)
                .reset_index())

plt.figure(dpi=500)
plt.title('Valor médio do aluguel por região', loc='left', fontsize=18)
sn.barplot(x='Regiao', y='Valor', data=df_grouped, hue='Regiao')
plt.xlabel('Regiao', fontsize = 13)
sn.despine()
plt.show()

#%%