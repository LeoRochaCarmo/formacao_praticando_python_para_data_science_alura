#%%

'''

Estamos trabalhando com o mesmo conjunto de dados contendo informações sobre atletas, já no formato de tuplas.

Queremos classificar os atletas com base em seu IMC (Índice de Massa Corporal) como "Peso Normal" ou "Sobrepeso". 
Porém, dessa vez queremos uma lista mais elaborada. O cálculo do IMC pode ser feito com a fórmula:

IMC = peso / altura².

Utilizando list comprehension, crie uma nova lista contendo tuplas no formato:

(nome_do_atleta, "Peso Normal" ou "Sobrepeso")

Se o IMC do atleta for maior que 25, ele será classificado como "Sobrepeso". Caso contrário, será classificado como "Peso Normal".

Imprima a lista resultante. Dica: Você pode usar if e else no list comprehension para realizar a tarefa.

'''

#%% 

atletas = [
    ("Maria Silva", 1.75, 65), ("João Santos", 1.80, 72),
    ("Ana Pereira", 1.68, 58), ("Pedro Oliveira", 1.92, 85),
    ("Carlos Lima", 1.85, 78), ("Beatriz Souza", 1.70, 60), 
    ("Fernanda Costa", 1.62, 55), ("Lucas Almeida", 1.88, 82), 
    ("Rafaela Gomes", 1.74, 63), ("Gustavo Ferreira", 1.90, 88), 
    ("Larissa Rocha", 1.66, 57), ("Henrique Nunes", 1.83, 76), 
    ("Juliana Martins", 1.72, 90), ("Ricardo Carvalho", 1.86, 80), 
    ("Sofia Alves", 1.64, 54), ("Matheus Ribeiro", 1.89, 84), 
    ("Camila Duarte", 1.69, 81), ("Gabriel Monteiro", 1.77, 73), 
    ("Eduarda Farias", 1.71, 62), ("Thiago Mendes", 1.84, 79),
]

classificao_imcs = [
    (atleta[0], "Sobrepeso" if ((atleta[2] / atleta[1]**2) > 25) else "Peso Normal")
    for atleta in atletas
    ]

print("CLASSIFICAÇÃO DOS ATLETAS PELO IMC")
print(*classificao_imcs, sep='\n')

# %%
