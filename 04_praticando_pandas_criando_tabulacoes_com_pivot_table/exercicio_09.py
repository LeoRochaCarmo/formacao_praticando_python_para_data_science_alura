#%%

'''
Agora que já exploramos como o ano de fabricação e o tipo de transmissão afetam o valor dos automóveis, 
vamos mergulhar em uma análise mais detalhada relacionando o estilo do automóvel com várias características 
de desempenho e consumo. Este tipo de análise pode ajudar a entender melhor como características técnicas 
podem influenciar o valor de mercado dos automóveis.

O objetivo desta atividade é usar o método pivot_table() para agrupar os dados pelo estilo do automóvel e 
calcular o preço médio, juntamente com a média de outras características importantes: potência do motor, 
número de cilindros, consumo na estrada e consumo na cidade.

Além disso, arredonde os resultados médios para facilitar a interpretação e ordene a tabela resultante pelo 
Valor($) em ordem decrescente para ver quais estilos de automóveis possuem maior valor médio.
'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df.head()

# %%

pivot_estilo = (df.pivot_table(values=['Valor($)','Potencia_motor', 'Cilindros_motor', 
                                       'Consumo_estrada_milhas', 'Consumo_cidade_milhas'],
                              index='Estilo')
                  .round() 
                  .sort_values('Valor($)', ascending=False))

pivot_estilo

# %%
