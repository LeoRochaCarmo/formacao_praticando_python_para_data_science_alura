#%%

'''
Você é responsável pelo setor de tecnologia de uma biblioteca pública e está trabalhando em um sistema de 
categorização de livros com base no ano de publicação.

Agora, você precisa classificar os livros em duas categorias:

"Clássico": Livros publicados antes do ano 2000.
"Moderno": Livros publicados no ano 2000 ou depois.
Utilizando list comprehension com if e else, crie uma nova lista contendo tuplas no formato:

(título_do_livro, "Clássico" ou "Moderno")

'''

#%%

livros = [
    ("Dom Quixote", 1605), ("Orgulho e Preconceito", 1813), 
    ("O Grande Gatsby", 1925), ("Cem Anos de Solidão", 1967), 
    ("1984", 1949), ("Harry Potter e a Pedra Filosofal", 1997), 
    ("O Senhor dos Anéis", 1954), ("A Revolução dos Bichos", 1945), 
    ("O Apanhador no Campo de Centeio", 1951), ("O Código Da Vinci", 2003), 
    ("Jogos Vorazes", 2008), ("A Culpa é das Estrelas", 2012), 
    ("Duna", 1965), ("A Menina que Roubava Livros", 2005), 
    ("O Hobbit", 1937), ("Moby Dick", 1851), ("Drácula", 1897), 
    ("Frankenstein", 1818), ("A Odisséia", -800),  # Ano fictício para livros clássicos antigos
    ("Hamlet", 1600),
]

classificacao_livros = [
    (livro[0], "Clássico" if livro[1] < 2000 else "Moderno")
    for livro in livros
]

print("CLASSIFICAÇÃO DOS LIVROS")
print(*classificacao_livros, sep='\n')