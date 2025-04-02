#%%

'''
Você trabalha em uma empresa de e-commerce e recebeu o desafio de calcular o Ticket Médio por 
Cliente para cada pedido registrado no sistema. O Ticket Médio é definido como o valor total 
do pedido dividido pelo número de clientes que participaram da compra 
(neste caso, sempre será 1 cliente por pedido, mas vamos deixar o cálculo genérico para casos futuros).

O DataFrame contém as seguintes colunas iniciais:

PedidoID: Identificador único do pedido.
Cliente: Nome do cliente que realizou o pedido.
ValorTotal: Valor total do pedido (em reais).
QuantidadeItens: Quantidade de itens comprados no pedido.

Sua tarefa é:
1 - Criar uma nova coluna chamada TicketMedio, que será calculada como:
Ticket Médio: Ticket Médio = Valor Total / Quantidade de Itens.

2 - Exibir as colunas PedidoID, Cliente, ValorTotal, QuantidadeItens e a nova coluna TicketMedio.

Objetivo:
1 - Crie a nova coluna TicketMedio.
2 - Exiba as colunas PedidoID, Cliente, ValorTotal, QuantidadeItens e TicketMedio.

A saída esperada deve ser semelhante ao seguinte:

   PedidoID   Cliente  ValorTotal  QuantidadeItens  TicketMedio
0       101     Alice      150.00               3    50.000000
1       102     Bruno      200.00               4    50.000000
2       103     Carla      300.00               6    50.000000
3       104    Daniel      120.00               2    60.000000
4       105   Eduarda      500.00              10    50.000

'''

#%%

import pandas as pd

dados = {
    'PedidoID': [101, 102, 103, 104, 105],
    'Cliente': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
    'ValorTotal': [150.00, 200.00, 300.00, 120.00, 500.00],
    'QuantidadeItens': [3, 4, 6, 2, 10]
}

df = pd.DataFrame(dados)

df['TicketMedio'] = df['ValorTotal'] / df['QuantidadeItens']

df

# %%
