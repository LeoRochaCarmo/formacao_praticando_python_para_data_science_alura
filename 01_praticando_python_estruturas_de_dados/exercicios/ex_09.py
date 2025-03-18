#%%

'''
Você recebeu uma solicitação para atualizar o dicionário catalogo, pois agora todos os anos de 
publicação dos livros devem ser convertidos para o número de anos que se passaram desde o 
lançamento até o ano atual (2025).

Usando dict comprehension, crie um novo dicionário chamado livros_atualizados, onde cada livro 
terá o mesmo título e autor, mas o campo "ano" será substituído pelo número de anos que se 
passaram desde o lançamento até 2025.

O dicionário resultante deverá ter o seguinte formato:

{
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 420},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 212},
    ...
}
'''

#%%

import json

catalogo = {
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
    "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
    "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "ano": 1967},
    "1984": {"autor": "George Orwell", "ano": 1949},
    "Harry Potter e a Pedra Filosofal": {"autor": "J.K. Rowling", "ano": 1997},
    "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
    "A Revolução dos Bichos": {"autor": "George Orwell", "ano": 1945},
    "O Apanhador no Campo de Centeio": {"autor": "J.D. Salinger", "ano": 1951},
    "O Código Da Vinci": {"autor": "Dan Brown", "ano": 2003},
}

livros_atualizados = {
    livro: {**info, 'ano': 2025 - info['ano']}
    for livro, info in catalogo.items()

}

print(json.dumps(livros_atualizados, indent=4, ensure_ascii=False))
# %%
