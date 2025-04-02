#%%

'''
Você recebeu o desafio de calcular o Índice de Altura Relativa de cada planta 
no conjunto de dados. Este índice é uma medida que compara a altura média de 
cada planta com a maior altura média registrada no conjunto de dados.

O cálculo do Índice de Altura Relativa será feito da seguinte forma:

Fórmula: Índice de Altura Relativa = Altura Média / Maior Altura Média.

Sua tarefa é:

Identificar a maior altura média no DataFrame.
Criar uma nova coluna chamada IndiceAlturaRelativa que contenha o índice calculado para cada planta.
Exibir as colunas Especie, AlturaMedia e IndiceAlturaRelativa.

Objetivo:

1 - Calcule a maior altura média no DataFrame.

2 - Crie uma nova coluna chamada IndiceAlturaRelativa, calculada como:

Fórmula: Índice de Altura Relativa = Altura Média / Maior Altura Média.

3 - Exiba as colunas Especie, AlturaMedia e IndiceAlturaRelativa.

A saída esperada deve ser semelhante ao seguinte:

               Especie  AlturaMedia  IndiceAlturaRelativa
0     Mangifera indica           15                 0.375
1  Eucalyptus globulus           30                 0.750
2     Pinus elliottii           25                 0.625
3  Anacardium occidentale           12                 0.300
4       Coffea arabica            3                 0.075

'''

#%%

import pandas as pd

dados = {
    'Especie': ['Mangifera indica', 'Eucalyptus globulus', 'Pinus elliottii', 'Anacardium occidentale',
                'Coffea arabica', 'Hevea brasiliensis', 'Carica papaya', 'Theobroma cacao',
                'Cocos nucifera', 'Bertholletia excelsa'],
    'Regiao': ['Norte', 'Sul', 'Leste', 'Norte', 'Sul', 'Oeste', 'Leste', 'Norte', 'Oeste', 'Norte'],
    'AlturaMedia': [15, 30, 25, 12, 3, 20, 5, 10, 18, 40]
}

df = pd.DataFrame(dados)

df['IndiceAlturaRelativa'] = df['AlturaMedia'] / df['AlturaMedia'].max()
df[['Especie', 'AlturaMedia', 'IndiceAlturaRelativa']].head()

# %%
