#%%

'''
Você trabalha como analista de dados em uma empresa de marketing digital e recebeu um 
DataFrame contendo posts de redes sociais. O objetivo é analisar o conteúdo e as 
métricas desses posts. O DataFrame contém as seguintes colunas iniciais:

Texto: Conteúdo do post
Horário: Horário de publicação (formato HH:MM)
Hashtags: Lista de hashtags usadas (separadas por vírgulas)
Caracteres_Emoji: String contendo emojis usados no post

Sua tarefa é:
Usar o método apply para criar uma nova coluna chamada Período_Dia, que classifica o horário da postagem em:
"Madrugada" (00:00 - 05:59)
"Manhã" (06:00 - 11:59)
"Tarde" (12:00 - 17:59)
"Noite" (18:00 - 23:59)
Usar o método apply para criar uma coluna Análise_Conteúdo que retorna um dicionário com:
Número de hashtags utilizadas
Número de emojis no post
Comprimento do texto
Exibir um DataFrame organizado com as análises.
'''

#%%

import pandas as pd

dados = {
    'Texto': [
        "Bom dia! ☀️ Começando mais uma semana produtiva!",
        "Novo produto chegando! 🎉 #novidade #lancamento",
        "Promoção relâmpago ⚡ Aproveitem! #promo #desconto",
        "Boa noite pessoal! 🌙 Até amanhã! #boanoite",
        "Dica do dia: 💡 Mantenha-se hidratado! #saude #bemestar"
    ],
    'Horário': ['07:30', '15:45', '12:20', '22:15', '10:00'],
    'Hashtags': ['', 'novidade,lancamento', 'promo,desconto', 'boanoite', 'saude,bemestar'],
    'Caracteres_Emoji': ['☀️', '🎉', '⚡', '🌙', '💡']
}

# Função para determinar período do dia
def get_periodo(horario):
    hora = int(horario.split(':')[0])
    if 0 <= hora < 6:
        return 'Madrugada'
    elif 6 <= hora < 12:
        return 'Manhã'
    elif 12 <= hora < 18:
        return 'Tarde'
    else:
        return 'Noite'

# Função para análise do conteúdo
def analisar_conteudo(row):
    num_hashtags = len([tag for tag in row['Hashtags'].split(',') if tag])
    num_emojis = len(row['Caracteres_Emoji'])
    comprimento_texto = len(row['Texto'])
    
    return {
        'num_hashtags': num_hashtags,
        'num_emojis': num_emojis,
        'comprimento_texto': comprimento_texto
    }


df = pd.DataFrame(dados)

df['Periodo_Dia'] = df['Horário'].apply(get_periodo)
df['Analise_Conteudo'] = df.apply(analisar_conteudo, axis=1)
df

# %%