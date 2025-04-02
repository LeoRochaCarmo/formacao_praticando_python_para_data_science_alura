#%%

'''
Verônica está avaliando um conjunto de dados relacionados ao cadastro de eventos que terão a 
cobertura da empresa em que ela trabalha. Ao observar o conjunto ela percebeu que algumas 
linhas das colunas 'Data' e 'Local' estavam sem informações.

Para o planejamento da cobertura dos eventos, é essencial que as informações de 'Data' e 'Local' 
estejam preenchidas, pois são fundamentais para identificar quando e onde o evento ocorrerá. 
Outras colunas podem ser opcionais.

Para que Verônica consiga avaliar adequadamente o conjunto de dados e planejar a cobertura, 
ela precisa ter apenas os eventos com informações completas em 'Data' e 'Local'. 

Como ela pode fazer isso?
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_8.csv')

df.dropna(subset=['Data', 'Local'], inplace=True)

df