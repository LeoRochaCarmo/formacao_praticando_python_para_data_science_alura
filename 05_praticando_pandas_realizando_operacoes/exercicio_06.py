#%%

'''
Você recebeu um conjunto de dados contendo informações de peso e altura de diferentes pessoas. 
O objetivo é calcular o IMC de cada pessoa e classificá-las em categorias de acordo com a 
tabela de classificação da Organização Mundial da Saúde (OMS).

Sua tarefa é:
1 - Criar uma função chamada categoriza_imc que classifique o IMC nas seguintes categorias:
"Abaixo do peso": IMC menor que 18.5.
"Peso normal": IMC entre 18.5 e 24.9 (inclusive).
"Sobrepeso": IMC entre 25 e 29.9 (inclusive).
"Obesidade Grau 1": IMC entre 30 e 34.9 (inclusive).
"Obesidade Grau 2": IMC entre 35 e 39.9 (inclusive).
"Obesidade Grau 3": IMC maior ou igual a 40.

2 - Calcular o IMC para cada pessoa usando a fórmula:
IMC = peso / altura².

3 - Criar uma nova coluna chamada Categoria_IMC que armazene a classificação do IMC de cada pessoa.

4 - Exibir as colunas Pessoa, Peso, Altura, IMC e Categoria_IMC.

Objetivo:

Criar uma função chamada categoriza_imc para classificar o IMC conforme as faixas descritas acima.
Calcular o IMC de cada pessoa e adicionar uma nova coluna IMC ao DataFrame.
Aplicar a função à coluna IMC para criar a nova coluna Categoria_IMC.
Exibir as colunas Pessoa, Peso, Altura, IMC e Categoria_IMC.
A saída esperada deve ser semelhante ao seguinte:

      Pessoa  Peso  Altura        IMC       Categoria_IMC
0       Ana    50    1.60  19.531250       Peso normal
1     Bruno    80    1.75  26.122449         Sobrepeso
2     Carla    70    1.68  24.801587       Peso normal
3    Daniel    95    1.80  29.320988         Sobrepeso
4   Eduarda    60    1.55  24.973985       Peso normal
5    Felipe   110    1.90  30.468749  Obesidade Grau 1
6  Gabriela    45    1.50  20.000000       Peso normal
7  Henrique   130    1.85  37.974684  Obesidade Grau 2

'''

#%%

import pandas as pd

dados = {
    'Pessoa': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Peso': [50, 80, 70, 95, 60, 110, 45, 130],
    'Altura': [1.60, 1.75, 1.68, 1.80, 1.55, 1.90, 1.50, 1.85]
}

df = pd.DataFrame(dados)

def categoria_imc(imc):
    if imc <= 18.5:
        return 'Abaixo do Peso'
    elif imc <= 24.9:
        return 'Peso Normal'
    elif imc <= 29.9:
        return 'Sobrepeso'
    elif imc <= 34.9:
        return 'Obesidade Grau 1'
    elif imc <= 39.9:
        return 'Obesidade Grau 2'
    
    return 'Obesidade Grau 3'

df['IMC'] = df['Peso'] / df['Altura'] ** 2
df['Categoria_IMC'] = df['IMC'].apply(categoria_imc)

df

# %%