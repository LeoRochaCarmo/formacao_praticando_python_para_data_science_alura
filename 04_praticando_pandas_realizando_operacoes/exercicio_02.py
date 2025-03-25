#%%
'''
Sua tarefa agora é identificar plantas de grande porte.

Para isso, foi definido o seguinte critério:

Uma planta é considerada "de grande porte" se sua altura média for maior que 20 metros.
Sua tarefa é criar uma nova coluna no DataFrame chamada "GrandePorte", que indique se 
cada planta atende ao critério de grande porte. Essa coluna deve conter valores True 
(se a planta for de grande porte) ou False (caso contrário).

Objetivo:

Crie uma nova coluna chamada "GrandePorte" no DataFrame, que indique se a planta é de grande porte 
(altura média > 20 metros).
Exiba as primeiras linhas do DataFrame com a nova coluna, incluindo apenas as colunas Especie, 
AlturaMedia e GrandePorte.
A saída esperada deve ser semelhante ao seguinte:

               Especie  AlturaMedia  GrandePorte
0     Mangifera indica           15        False
1  Eucalyptus globulus           30         True
2     Pinus elliottii           25         True
3  Anacardium occidentale           12        False
4       Coffea arabica            3        False

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

df['GrandePorte'] = df['AlturaMedia'].apply(lambda x: True if x > 20 else False)

df[['Especie', 'AlturaMedia', 'GrandePorte']].head()

# %%

# JEITO MAIS SIMPLES

df['GrandePorte'] = df['AlturaMedia'] > 20

df[['Especie', 'AlturaMedia', 'GrandePorte']].head()

# %%
