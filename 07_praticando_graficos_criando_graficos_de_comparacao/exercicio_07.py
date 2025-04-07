#%%

'''
Agora, vamos explorar dados da área médica, com foco em informações relacionadas a doenças cardíacas. 
Nesta atividade, você analisará a distribuição dos tipos de dor torácica em um conjunto de dados 
de pacientes, criando um gráfico que visualize a frequência de cada categoria. 
Essa análise permitirá uma melhor compreensão dos padrões presentes nos dados.

Sua tarefa será:
Carregar os dados;
Contar quantos pacientes pertencem a cada categoria de dor torácica;
Ordenar as categorias do maior para o menor valor;
Criar um gráfico adequado para visualizar essa distribuição;
Personalizar o gráfico para torná-lo mais informativo e fácil de interpretar.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/pacientes_doenca_cardiaca.csv'

df = pd.read_csv(url)

df_tipos_dor = df['Tipo_dor'].value_counts()

plt.figure(dpi=500)
plt.title('Qtde. de pacientes por categoria de dor', loc='left', fontsize=14)
sn.countplot(x='Tipo_dor', data=df ,order=df_tipos_dor.index, hue='Tipo_dor')
plt.xlabel('')
plt.ylabel('')
sn.despine()
plt.show()

#%%