segundos = int(input("Digite o tempo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60
print("Tempo: {}:{}:{}".format(horas,minutos,segundos))
