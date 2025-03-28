#%%

'''
Jorge, ao receber dados relacionados a pedidos feitos na empresa que trabalha, percebeu que 
alguns dos pedidos não continham uma data de entrega prevista registrada no momento do pedido, 
deixando valores ausentes no dataset.

Então, ele identificou que isso poderia ter acontecido por algum problema nos agendamentos. 
Para solucionar esse problema, ele decidiu assumir que os pedidos sem data de entrega 
herdarão a próxima data prevista no registro. Isso ocorre porque as previsões são frequentemente 
baseadas em lotes. Considerando isso, como Jorge poderia fazer o preenchimento dos prazos de entrega?
'''

#%%

import pandas as pd

df = pd.read_csv('.\\dados\\atividades_5.csv')

df['Data_Entrega_Prevista'] = df['Data_Entrega_Prevista'].bfill().ffill()

df