
#%%

'''
Por fim, vamos finalizar as atividades focando em uma análise detalhada de vários indicadores clínicos dos pacientes, 
agrupados por presença de doença cardíaca e sexo biológico. Exploraremos as médias de várias informações. 
Este exercício é fundamental para entender esses fatores em diferentes grupos.

Agrupe os dados por doença cardíaca e sexo biológico e aplique várias funções de agregação para calcular as 
médias das seguintes variáveis: idade, pressão arterial, colesterol, frequência cardíaca máxima, Depressão ST, 
Inclinação ST e número de vasos detectados por fluoroscopia.

Renomeie as colunas resultantes para indicar que contêm as médias das variáveis.

'''

#%%

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/pacientes_doenca_cardiaca.csv'

df = pd.read_csv(url)

agregacoes = {
    'Idade': 'mean',
    'Pressao_arterial': 'mean',
    'Colesterol': 'mean',
    'Frequencia_cardiaca_max': 'mean',
    'Depressao_ST': 'mean',
    'Inclinacao_ST': 'mean',
    'Numero_vasos_fluro': 'mean',
}

nomes_colunas = {
    col: 'Media_' + col
    for col in agregacoes.keys()
}

indicadores_clinicos = df.groupby(by=['Doenca_cardiaca', 'Sexo_biologico'], as_index=False).agg(agregacoes).rename(columns=nomes_colunas)

indicadores_clinicos

# %%
