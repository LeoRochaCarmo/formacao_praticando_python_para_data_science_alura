#%%

'''
Nesta atividade, vamos aprofundar a análise do impacto da doença cardíaca em diferentes tipos de dor no peito, correlacionando-os com o nível de depressão ST, 
um indicador comum usado em exames cardíacos. Este tipo de análise é crucial para entender como a doença cardíaca pode influenciar outros sintomas e resultados de exames.

Agrupe os dados pela presença de doença cardíaca e tipo de dor no peito, e calcule a média do exame Depressão_ST para cada grupo. 
Utilize o método unstack() para transformar os dados agrupados em uma tabela mais legível, facilitando a comparação entre os diferentes grupos.

'''
#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/pacientes_doenca_cardiaca.csv'

df = pd.read_csv(url)


doenca_cardiaca_e_dor_no_peito = df.groupby(by=['Doenca_cardiaca', 'Tipo_dor'])[['Depressao_ST']].mean().unstack()
doenca_cardiaca_e_dor_no_peito

# %%
