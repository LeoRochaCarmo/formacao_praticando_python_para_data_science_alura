#%%

'''
Aprofundando a análise das vendas, agora vamos explorar como as categorias de produtos se 
comportam em diferentes unidades da rede de lojas. Esta análise ajudará a entender melhor a 
interação entre localização e tipo de produto, fornecendo insights valiosos para otimização 
de estoque e estratégias de marketing regionalizadas.

Utilize o método pivot_table() para criar uma tabela que cruze as informações de unidade e 
categoria de produto, com o objetivo de calcular a soma do valor total de vendas para cada 
combinação de unidade e categoria.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_unidade_categoria = df.pivot_table(values='valor_total', 
                                       index=['unidade', 'categoria_produto'], 
                                       aggfunc='sum')
pivot_unidade_categoria

# %%
