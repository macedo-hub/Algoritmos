distancia = float(input("Digite a distância a ser percorrida (km): "))
consumo = float(input("Digite o consumo do veículo (km/l): "))
combustivel = distancia / consumo
print("Para percorrer {} Km serão necessários {:.1f} litros de
combustível".format(distancia,combustivel))
