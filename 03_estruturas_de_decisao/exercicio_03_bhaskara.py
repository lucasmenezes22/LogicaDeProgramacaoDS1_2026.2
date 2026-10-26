"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
a = float(input("digite valor de A"))
b = float(input("digite valor de B"))
c = float(input("digite valor de C"))

delta  = (b**2)-(4*a*c) 
if delta < a or a == 0: 
    print("impossivel de calcular")
else:
    X1 = (-b + delta**0.5) / (2*a)
    X1 = (-b + delta**0.5) / (2*a)
    print (f"{X1:.5f}")