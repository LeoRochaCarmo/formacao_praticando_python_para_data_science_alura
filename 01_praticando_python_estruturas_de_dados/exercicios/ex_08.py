#%%
'''
Agora que você já possui o dicionário catalogo com as informações dos livros, vamos realizar uma operação utilizando dict comprehension.
Crie um novo dicionário chamado livros_antigos contendo apenas os livros publicados antes do ano 1950. 
Utilize dict comprehension para realizar esta tarefa.
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

#%%

# Resolução do instrutor

# Filtrar livros antigos (publicados antes de 1950)
livros_antigos = {
    titulo: info
    for titulo, info in catalogo.items()
    if info["ano"] < 1950
}

# Imprimir os resultados
print("Livros antigos (antes de 1950):")
print(livros_antigos)


#%%

# Colocando os nomes das chaves na mão (jeito que eu fiz)

livros_antigos = {
    livro: {'autor': dados['autor'], 'ano': dados['ano']}
    for livro, dados in catalogo.items()
    if dados['ano'] < 1950
}

print(json.dumps(livros_antigos, indent=4, ensure_ascii=False))

#%%

# Colocando os nomes das chaves dinamicamente (usando walrus operator (:=))

livros_antigos = {
    livro: {
        primeira_chave: dados[primeira_chave],
        segunda_chave: dados[segunda_chave]
    }
    for livro, dados in catalogo.items()
    if (chaves := list(dados.keys())) and len(chaves) >= 2  # Captura as chaves
    for primeira_chave, segunda_chave in [(chaves[0], chaves[1])]
    if dados[segunda_chave] < 1950
}

print(json.dumps(livros_antigos, indent=4, ensure_ascii=False))

# %%


