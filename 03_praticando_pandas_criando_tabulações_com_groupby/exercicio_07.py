#%%

'''
Nesta atividade, vamos explorar um conjunto de dados que contém informações sobre pacientes que 
foram diagnosticados com ou sem doença cardíaca. Temos dados demográficos e informações de alguns exames médicos.

O primeiro desafio com esses dados será agrupá-los com base na presença/ausência de doença cardíaca e sexo biológico, 
e calcular as idades mínima, média e máxima para cada grupo. Esta análise ajudará a identificar se há padrões visíveis 
que associam idade e sexo biológico à prevalência de doença cardíaca nestes dados.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/pacientes_doenca_cardiaca.csv'

df = pd.read_csv(url)

estatistica_doenca_cardiaca = (df.groupby(by=['Doenca_cardiaca', 'Sexo_biologico'], as_index=False)['Idade']
                                  .agg(['min', 'mean', 'max']))

estatistica_doenca_cardiaca

# %%
