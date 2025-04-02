#%%

'''
Anteriormente, você praticou como identificar valores nulos e também descobriu como observar 
as linhas onde estão os valores nulos. Agora, você precisa avançar um pouco mais na identificação 
dos dados nulos para a manipulação deles com Pandas.

Com o mesmo conjunto de dados do exercício anterior, como você conseguiria identificar quantos valores nulos 
esse conjunto de dados tem em cada coluna? E como contar a quantidade total de nulos presentes no DataFrame?
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_1_2_3.csv')

total_valores_nulos = df.isna().sum().sum()

print(total_valores_nulos)

# %%
