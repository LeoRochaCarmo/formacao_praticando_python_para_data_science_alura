#%%

import pandas as pd
import json

#%%

# Exercício 01

'''
João possui um arquivo JSON contendo dados sobre as vendas da loja onde trabalha, salvo em sua máquina. 
Ele deseja processar esse arquivo no Python utilizando a biblioteca Pandas.
Ajude João a criar um código que carregue o arquivo JSON como um DataFrame.
'''

df_01 = pd.read_json('.\\dados\\questao_1.json')
df_01

# %%

# Exercício 02

'''
Márcia recebeu dois conjuntos de dados em formato JSON. O primeiro conjunto contém informações referentes 
à primeira semana do mês na loja onde trabalha, e o segundo conjunto refere-se à segunda semana.

Márcia deseja saber a forma mais eficiente de carregar esses dados no Python para manipulá-los como DataFrames. 
Analise os conjuntos e indique a melhor abordagem para resolver o problema.
'''

df_02 = pd.read_json('.\\dados\\questao_2_1.json')
df_03 = pd.read_json('.\\dados\\questao_2_2.json')

df_03

# %%

# Exercício 03 (JEITO 1 -> FORMA MAIS BRUTA. NA RAÇA)

'''
Thais utilizou a função pd.read_json para carregar um arquivo JSON recebido em sua empresa. 
No entanto, ela notou que não conseguia acessar corretamente todos os dados do arquivo no DataFrame.

Um problema identificado foi que a coluna detalhes_compra apresentava informações importantes em 
formato de dicionário, dificultando a manipulação dos dados.

Ajude Thais a acessar todas as colunas e informações disponíveis nos dados.

'''

with open ('.\\dados\\questao_3.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    
df_04 = pd.json_normalize(dados, sep='_')

# Criei uma lista com os nomes das colunas
colunas = df_04.columns.to_list()

# Criei essa função como extra -> remove 'detalhes_' das colunas
def remove_strings(colunas, texto):
    colunas_atualizadas = []
    for i in colunas:
        if texto in i:
            texto_alterado = '_'.join(i.split('_')[1::])
            colunas_atualizadas.append(texto_alterado)
        else:
             colunas_atualizadas.append(i)
    return colunas_atualizadas

# Troquei os nomes das colunas pelo resultado gerado da função
df_04.columns = remove_strings(colunas, 'detalhes_')       
df_04

#%%

# Exercício 03 (JEITO 2 - LIST COMPREHESION PARA RENOMEAR COLUNAS DO DF)

with open ('.\\dados\\questao_3.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
 
df_03 = pd.json_normalize(dados, sep='_')

texto_para_remover = 'detalhes_compra_'
colunas = [col.replace(texto_para_remover, '') for col in df_03.columns]

df_03.columns = colunas
df_03

# %%

# Exercício 04

'''
Fábio recebeu um conjunto de dados relacionados às vendas da empresa onde trabalha. 
Ao inspecionar o arquivo, percebeu que se tratava de um JSON com uma estrutura aninhada de 3 níveis.

Como Fábio nunca trabalhou com a normalização de arquivos JSON, ele não sabe como lidar com um arquivo
aninhado dessa complexidade. O que Fábio pode fazer para transformar esse JSON em um conjunto de 
dados utilizável?
'''
with open ('.\\dados\\questao_4.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Normalizando o arquivo JSON
df_04 = pd.json_normalize(dados, sep='_')

# Gerando listas com novos nomes para as colunas.
# Removendo 'cliente_', 'detalhes_compra_' e 'produto_' dos nomes
colunas = [
    (col.replace('cliente_', '')
        .replace('detalhes_compra_', '')
        .replace('produto_', ''))
       for col in df_04.columns]

# Renomeando as colunas no dataframe original
df_04.columns = colunas

# Vizualizando dataframe
df_04

# %%
