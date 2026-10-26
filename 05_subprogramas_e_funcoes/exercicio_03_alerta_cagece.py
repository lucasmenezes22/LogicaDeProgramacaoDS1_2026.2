"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
from operator import truediv


def emitir_alerta_fatura(nome_do_cliente, valor, data_de_vencimento):
    print(f"Presado(a) {nome_do_cliente}, sua fatura da cagece no valo de R$ {valor} vence no dia {data_de_vencimento}.")
    return True
alerta_fatura = emitir_alerta_fatura ("arthur pixica", 350, "25/10")