#%%

'''
Após examinar como características específicas dos imóveis influenciam os preços de aluguel em diferentes regiões, 
vamos agora focar em uma perspectiva temporal, considerando o ano de construção dos imóveis. O objetivo é compreender como 
a idade das construções influencia os preços de aluguel.

Agrupe os dados pelo ano do imóvel e calcule a média do valor de aluguel para cada ano. Isso permitirá que você visualize 
a variação dos preços de aluguel ao longo do tempo e identifique padrões de aumento, estabilidade ou diminuição.

Para simplificar a análise, você pode criar um gráfico de linhas diretamente com a biblioteca Pandas. 
Basta utilizar o método plot(kind='line') na variável que contém os dados agrupados, 
e o gráfico será gerado automaticamente."


'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url)

tendencia_anual_imovel = df.groupby(by='Ano')[['Valor']].mean()

tendencia_anual_imovel.plot(kind='line')

# %%
