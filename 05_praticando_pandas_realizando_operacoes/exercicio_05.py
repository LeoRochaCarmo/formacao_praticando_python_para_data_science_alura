#%%

'''
Você recebeu um conjunto de dados com as notas finais de alunos em uma disciplina. 
O objetivo é categorizar o desempenho dos alunos com base em suas notas finais, 
utilizando uma função personalizada aplicada com o método apply.

Sua tarefa é:
Criar uma função chamada categoriza_desempenho que classifique os alunos nas seguintes categorias:
"Excelente": Para notas maiores ou iguais a 90.
"Bom": Para notas entre 70 (inclusive) e 89.
"Regular": Para notas entre 50 (inclusive) e 69.
"Insuficiente": Para notas abaixo de 50.
Aplicar a função à coluna NotaFinal para criar uma nova coluna chamada Categoria_Desempenho.
Exibir as colunas Aluno, NotaFinal e Categoria_Desempenho.

Objetivo:

Criar uma função chamada categoriza_desempenho para classificar as notas conforme as faixas descritas acima.
Aplicar a função à coluna NotaFinal usando o método apply.
Exibir as colunas Aluno, NotaFinal e Categoria_Desempenho.
A saída esperada deve ser semelhante ao seguinte:

      Aluno  NotaFinal Categoria_Desempenho
0     Alice         95           Excelente
1     Bruno         82                 Bom
2     Carla         67             Regular
3    Daniel         45        Insuficiente
4   Eduarda         78                 Bom
5    Felipe         88                 Bom
6  Gabriela         50             Regular
7  Henrique         30        Insuficiente
'''

#%%

import pandas as pd

dados = {
    'Aluno': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'NotaFinal': [95, 82, 67, 45, 78, 88, 50, 30]
}

df = pd.DataFrame(dados)

def categoria_desempenho(nota):
    if nota >= 90:
        return 'Excelente'
    elif nota >= 70 and nota <= 89:
        return 'Bom'
    elif nota >= 50 and nota <= 69:
        return 'Regular'
    
    return 'Insuficiente'

df['CategoriaDesempenho'] = df['NotaFinal'].apply(categoria_desempenho)

df
# %%
