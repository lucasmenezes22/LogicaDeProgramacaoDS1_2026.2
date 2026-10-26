"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valorInvestido = float(input("valor investido: "))
numero_de_clientes_obitidos = int(input("clientes obtidos: "))
cpc = valorInvestido / numero_de_clientes_obitidos
print(f"custo por clique foi de: R$ {cpc:.2f}")
