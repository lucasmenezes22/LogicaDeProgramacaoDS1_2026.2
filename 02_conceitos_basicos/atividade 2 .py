# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pesso
# 4. Imprima formatado usando f-string
valor_da_conta = float(input("insira o valor da conta: "))
numero_de_pessoas = int(input("insira o numero de pessoas: "))
valor_por_pessoa = valor_da_conta / numero_de_pessoas
print(f"o valor por pessoa é:{valor_por_pessoa:.2f} ")  