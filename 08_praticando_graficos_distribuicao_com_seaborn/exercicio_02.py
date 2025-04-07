#%%
'''
Lucas é um analista de vendas em uma empresa de e-commerce. Ele recebeu um conjunto de dados 
com informações sobre os valores dos pedidos de 500 clientes, além de informações complementares 
como número de itens no pedido, tempo gasto no site (em minutos) e região do cliente. 
Lucas quer analisar a distribuição dos valores dos pedidos para entender quais faixas de preço 
são mais comuns entre os clientes.

Como Lucas conseguiria visualizar a distribuição dos valores dos pedidos? 
Considere os dados complementares e sugira possíveis análises futuras com base nos resultados.
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_2.csv')

plt.figure(figsize=(10,6), dpi=400)
plt.title('Distribuição dos valores dos pedidos', fontsize=16)
plt.ylabel('Frequência')
sn.histplot(df['Valor do Pedido (R$)'], bins=20)
sn.despine()
plt.tight_layout()
plt.show()