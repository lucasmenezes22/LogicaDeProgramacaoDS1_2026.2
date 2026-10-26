"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    return (distancia_km / consumo_kml * preco_combustivel)
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao

distancia = float(input("distancia_km: "))
consumo = float(input("consumo_kml: "))
preco = float(input("diaria_alimentacao: "))

pessoas = int(input("quantidade de pessoas"))
dias = int(input("quantidade dias"))
diaria = int(input("custo por diaria"))

alimentacao = calcular_custo_alimentacao (pessoas, dias, diaria)
transporte = calcular_custo_transporte (distancia, consumo, preco)
total = transporte + alimentacao 
print(f"custo transporte: {transporte:.2f}")
print(f"custo alimentacao:{alimentacao:.2f}")
print(f"custo total:{total:.2f}")