#%%
'''
Você trabalha no departamento de recursos humanos e precisa analisar os salários dos colaboradores. 
Você recebeu um conjunto de dados com os salários anuais (em reais) de 300 funcionários e, 
para identificar possíveis padrões, como faixas salariais mais comuns ou discrepâncias 
que mereçam atenção, você precisa visualizar a distribuição desses salários.

Crie um histograma utilizando Seaborn para visualizar a distribuição 
dos salários anuais. O que você pode observar sobre a distribuição?
'''

#%%

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('.\\dados\\atividade_1.csv')

plt.figure(figsize=(10,6), dpi=400)
plt.title('Distribuição dos salários anuais', fontsize=16)
plt.ylabel('Frequência')
sn.histplot(df['Salário Anual (R$)'], bins=20)
sn.despine()
plt.tight_layout()
plt.show()

