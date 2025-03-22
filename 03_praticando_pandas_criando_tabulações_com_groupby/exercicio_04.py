#%%

'''
Após explorar as estatísticas descritivas dos valores de aluguel por região, nosso próximo passo é entender como a ausência/presença 
de uma piscina no prédio influencia o preço de aluguel em diferentes regiões de São Paulo. 
Esta análise ajudará a entender melhor as preferências do mercado e poderá ser usada para orientar estratégias de precificação e marketing.

Agrupe os dados por região e piscina e calcule a média dos preços de aluguel. Esta abordagem mostrará como as piscinas afetam
os preços de aluguel em diferentes áreas da cidade.


'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

valor_piscina_regiao = df.groupby(by=['Regiao', 'Piscina'], as_index=False)[['Valor']].mean()

valor_piscina_regiao

# %%