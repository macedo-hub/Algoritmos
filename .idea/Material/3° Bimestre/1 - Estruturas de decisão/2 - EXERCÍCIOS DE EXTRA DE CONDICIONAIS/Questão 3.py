numero = int(input("Digite um número: "))
if (numero >= 0 and numero < 10):
    print("O número digitado possui um dígito.")
elif (numero >= 10 and numero < 100):
print("O número digitado possui dois dígitos.")
elif (numero >= 100 and numero < 1000):
print("O número digitado possui três dígitos.")
else:
print("O número digitado possui mais que três dígitos.")
