"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:

valores_pasitivos = 0
for i in range(6):
    valor = float(input("digite um numero: "))
    if valor >0: 
# valores_positivos: append("valor") 

# quantidade_positivos = len("valores_positivos")

# print(f"{quantidade_positivos} valores positivos ")
        valores_pasitivos   +=1

print(f"quantidade de numeros positivos {valores_pasitivos}")


# if quantidade_positivos >0:
#     media = sum("valores positivos") / quantidade_positivos 
#     print(f"{media:.1f}")