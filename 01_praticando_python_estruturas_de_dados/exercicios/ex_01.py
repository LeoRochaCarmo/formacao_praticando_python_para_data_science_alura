#%%

'''
Você é um cientista de dados trabalhando para um comitê olímpico. Você recebeu uma lista com informações de atletas de diversas modalidades,
 incluindo nome, altura (em metros) e peso (em kg). Esses dados estão organizados de forma um pouco confusa, dificultando a análise. 
 Sua tarefa é usar um loop for em Python para processar essa lista e organizar as informações de cada atleta em um formato mais estruturado, 
 facilitando futuras análises estatísticas e comparações.
'''

'''
Objetivo:
Utilizando um loop for, crie um programa que processe a lista atletas e para cada atleta, imprima as informações no seguinte formato:
'''

# Nome: Maria Silva
# Altura: 1.75 m
# Peso: 65 kg
# --------------------

# Isso deve ser repetido para todos os atletas presentes na lista. Seu código deve funcionar independentemente do número de atletas presentes na lista.

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

for atleta in atletas:
    lista_informacoes = []
    for informacoes in atleta:
        lista_informacoes.append(informacoes)
    print(f'Nome: {lista_informacoes[0]}')
    print(f'Altura: {lista_informacoes[1]} m')
    print(f'Peso: {lista_informacoes[2]} kg')
    print('--------------------------')


# %%

for atleta in atletas:
    nome = atleta[0]       # Primeiro elemento da lista é o nome
    altura = atleta[1]     # Segundo elemento da lista é a altura
    peso = atleta[2]       # Terceiro elemento da lista é o peso

    # Exibição formatada das informações do atleta
    print(f"Nome: {nome}")
    print(f"Altura: {altura} m")
    print(f"Peso: {peso} kg")
    print("-" * 20)  # Linha separadora