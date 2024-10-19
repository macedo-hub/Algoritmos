dist = int(input("Digite uma distância em km: "))
if (dist >= 1 and dist <= 25):
    custo = dist * 2
elif (dist >= 26 and dist <= 50):
custo = dist * 3
elif (dist >= 51 and dist <= 100):
custo = dist * 4
else:
custo = dist * 5
print("O custo total da viagem foi: R$ {:.2f}.".format(custo))
