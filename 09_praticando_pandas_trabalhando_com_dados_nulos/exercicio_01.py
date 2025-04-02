#%%

'''
Você recebeu um conjunto de dados em formato csv para trabalhar com dados contidos nele. 
Ao carregar o arquivo para o ambiente Python como um DataFrame você nota que ele contém alguns valores nan:

De que forma você pode identificar os dados nulos existentes no DataFrame? 
Faça a visualização de pelo menos uma linha que tenha dados nulos.
'''
#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_1_2_3.csv')

df[df.isnull().any(axis=1)]

# %%
