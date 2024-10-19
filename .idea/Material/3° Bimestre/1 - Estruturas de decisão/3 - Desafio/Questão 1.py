altura = float(input("Digite a altura do reservatório (em metros): "))
largura = float(input("Digite a largura do reservatório (em metros): "))
comprimento = float(input("Digite o comprimento do reservatório (em metros): "))
consumo_diario = float(input("Digite o consumo médio diário (em litros): "))

capacidade_m3 = altura * largura * comprimento
capacidade_litros = capacidade_m3 * 1000
autonomia_dias = capacidade_litros / consumo_diario

print("\nCapacidade total do reservatório: {:.2f} metros cúbicos".format(capacidade_m3))
print("Capacidade total do reservatório: {:.2f} litros".format(capacidade_litros))
print("Autonomia do reservatório: {:.2f} dias".format(autonomia_dias))

if autonomia_dias < 2:
    classificacao = "Consumo elevado"
elif 2 <= autonomia_dias < 7:
    classificacao = "Consumo moderado"
else:
    classificacao = "Consumo reduzido"

print("Classificação do consumo: {}".format(classificacao))
