'''
Continuando o seu trabalho como cientista de dados do comitê olímpico, agora você deve reorganizar a lista de atletas, 
em uma lista de tuplas, onde cada tupla representa um atleta e contém as informações de nome, altura e peso, respectivamente. 
Essa estrutura permitirá o acesso aos dados de cada atleta de forma mais eficiente, e que esses dados não possam mais ser modificados. 
Essa organização é crucial para etapas posteriores da análise, como o cálculo do IMC (Índice de Massa Corporal) 
de cada atleta e a identificação de padrões nos dados.

Objetivo:
Escreva um programa Python que converta a lista atletas em uma lista de tuplas, 
onde cada tupla contém o nome, altura e peso de um atleta. Imprima a lista de tuplas resultante.
'''

#%%

atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]

lista_de_tuplas = []

for atleta in atletas:
    lista_de_tuplas.append(tuple(atleta))

print(*lista_de_tuplas, sep='\n')

# %%
