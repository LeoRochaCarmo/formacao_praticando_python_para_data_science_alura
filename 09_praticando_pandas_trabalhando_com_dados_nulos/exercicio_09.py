#%%

'''
Letícia está estudando dados relacionados ao desempenho dos estudantes na plataforma de cursos em que ela trabalha. 
Observando os dados, ela notou que algumas linhas estavam completamente preenchidas com valores ausentes.

Letícia entende que os dados vazios que não preenchem todas as colunas não geram problema em seu estudo, 
apenas aquelas linhas que estão completamente ausentes. Como Letícia poderia remover somente 
as linhas que têm dados inteiramente nulos?
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_9.csv')

df.dropna(how='all', ignore_index=True, inplace=True)

df