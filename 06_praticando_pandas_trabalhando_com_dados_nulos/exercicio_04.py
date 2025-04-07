#%%
'''
Ana precisa analisar um conjunto de dados que informa as temperaturas máximas na cidade de São Paulo 
por um período específico de tempo. Por problemas nos sensores meteorológicos, em alguns dias não 
foi registrada a temperatura máxima, resultando em valores ausentes no conjunto de dados.

Segundo informações do centro meteorológico, as temperaturas máximas não tiveram uma diferença 
brusca de um dia para outro. Com isso, Ana entendeu que seria razoável aplicar a substituição 
das temperaturas máximas faltantes pelos valores dos dias anteriores.

Como Ana poderia fazer essa substituição?'
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_4.csv')

df['Temperatura_Maxima'] = df['Temperatura_Maxima'].ffill()

df

