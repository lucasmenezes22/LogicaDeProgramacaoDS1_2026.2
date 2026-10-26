"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia_total_pecorrida = float(input("distancia total pecorrida"))
total_de_combustivel_gasto = float(input("total de combustivel gasto"))
cpc = distancia_total_pecorrida / total_de_combustivel_gasto
print(f"consumo da moto foi de: litro {cpc:.1f }")