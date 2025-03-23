#%%

'''
Agora, vamos aprofundar nossa análise dos automóveis usados, explorando a relação entre o estilo 
do carro e o tamanho do veículo. Este tipo de informação é crucial para entender as preferências 
do consumidor e as tendências do mercado, especialmente quando consideramos diferentes segmentos de tamanho.

O objetivo desta atividade é usar o método pivot_table() para agrupar os dados pelo estilo do automóvel, 
definindo o tamanho dos automóveis como colunas. Como nem todos os estilos têm representantes em cada 
categoria de tamanho, você também precisará preencher os valores nulos com zero. 
Além disso, para facilitar a visualização e a comparação, ordene as colunas de tamanho na sequência: compacto, médio e grande.

Dica: Para ordenar as colunas, crie uma lista com a ordem desejada dos tamanhos: ['compacto', 'medio', 'grande']. 
Após criar a tabela, utilize esta lista para reorganizar as colunas do DataFrame. Isso é feito passando a lista como um índice 
ao selecionar as colunas do DataFrame. Essa técnica garante que a visualização dos dados seja mais organizada e facilita a 
comparação direta entre os diferentes tamanhos de veículos, proporcionando insights mais precisos e acessíveis.

'''
#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'

df = pd.read_csv(url)

df_na_tamanho = df['Tamanho'].isnull()

df[df_na_tamanho]

# %%

ordem_colunas = ['compacto', 'medio', 'grande']


pivot_estilo_tamanho = df.pivot_table(values='Valor($)', 
                                      index='Estilo', 
                                      columns='Tamanho', 
                                      aggfunc='count',
                                      fill_value=0)

pivot_estilo_tamanho = pivot_estilo_tamanho[ordem_colunas]

pivot_estilo_tamanho

# %%
