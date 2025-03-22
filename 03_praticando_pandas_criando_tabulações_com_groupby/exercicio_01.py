#%%

'''
Você está analisando dados de vendas em uma rede de lojas de departamentos e foi encarregado(a) de responder 
a algumas perguntas de negócio críticas para o planejamento estratégico da empresa. A primeira questão essencial 
é entender o desempenho das três unidades da rede, especificamente no que se refere ao valor total de vendas para o período.

O objetivo é obter a soma do valor total das vendas por unidade para identificar qual está performando melhor em t
ermos de geração de receita. Essa análise ajudará a liderança a tomar decisões informadas sobre possíveis investimentos, p
romoções e realocação de recursos.

Os dados estão disponíveis na seguinte url:

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

Sua missão nesta atividade é carregar os dados de vendas, examinar as informações disponíveis, e aplicar 
o método groupby() para agrupar e sumarizar o valor total de vendas por unidade.
'''

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url)

vendas_por_unidade = df.groupby(by=['unidade'],as_index=False)[['valor_total']].sum()
                
vendas_por_unidade

# %%
