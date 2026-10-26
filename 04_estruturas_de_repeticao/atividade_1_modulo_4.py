
numero = int(input("Digite um numero para ver a tabuada:"))

print(f"\ntabuada da mutiplicacao do {numero}:")
for i in range(1, 11):
    resultado = numero * i 
    print(f"{numero} * {i} = {resultado}")