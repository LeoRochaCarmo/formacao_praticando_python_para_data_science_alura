#%%

'''
Seu objetivo é criar um dicionário onde cada livro será representado por uma chave (o título do livro) 
e o valor será outro dicionário contendo as informações do autor e do ano de publicação. 
O dicionário final deve ter o seguinte formato:

{
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
    "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
    ...
}

Crie um dicionário chamado catalogo e organize os dados da lista livros no formato especificado.
'''

#%%

import json

livros = [
    ("Dom Quixote", "Miguel de Cervantes", 1605),
    ("Orgulho e Preconceito", "Jane Austen", 1813),
    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
    ("1984", "George Orwell", 1949),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
    ("A Revolução dos Bichos", "George Orwell", 1945),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951),
    ("O Código Da Vinci", "Dan Brown", 2003),
]

catalogo = {
    livro[0]:{"autor": livro[1], "ano": livro[2]}
    for livro in livros
}

print('CATÁLOGO DE LIVROS')


#  json.dumps() -> permite formatar a saída com espaçamento e quebras de linha.
# indent=4: Adiciona espaçamento de 4 espaços para melhorar a legibilidade.
# ensure_ascii=False: Mantém caracteres acentuados corretamente.

print(json.dumps(catalogo, indent=4, ensure_ascii=False))

# %%
