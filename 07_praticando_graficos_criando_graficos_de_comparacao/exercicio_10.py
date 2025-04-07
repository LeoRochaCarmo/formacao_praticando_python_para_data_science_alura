#%%

'''
Agora vamos analisar os dados de um e-commerce internacional, que vende diversos produtos para 
consumidores ao redor do mundo. Algumas categorias de produtos vendidos por esse e-commerce 
podem ter um desempenho muito melhor em um mercado do que em outro. Para otimizar as estratégias 
de vendas e marketing, eles precisam comparar as vendas (em milhões de dólares) de diferentes 
tipos de produtos em cada uma dessas regiões.

Sua tarefa será:
Carregar os dados;
Criar um gráfico adequado para visualizar essa comparação;
Personalizar o gráfico para torná-lo mais informativo e visualmente compreensível.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dataset_vendas.csv'

df = pd.read_csv(url)

fig, ax = plt.subplots()
plt.title('Vendas por categoria e região', loc='left', fontsize=14)
plt.ylabel('Vendas (milhões de doláres)', fontsize=10)
plt.xlabel('Categoria', fontsize=10)
sn.barplot(x='Categoria', y='Vendas', data=df, hue='Regiao')
plt.legend(title='Região')
for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=1.5)
sn.despine()
plt.show()

#%%