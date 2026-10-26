# TODO: Desenvolva o acumulador com parada no 0
soma = 0
print("digite os numeros que dejesa somar (ou digite o numero 0 para parar): ")

while True:
    numero = int(input("digite o numero:"))

    if numero == 0:
        break
    soma_total += numero
    print(f"\nEstrutura encerrada. A soma totaal acumulada é: {soma_total}")