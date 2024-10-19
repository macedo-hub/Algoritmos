numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
if (numero1 % numero2 == 0):
    print("{} é múltiplo de {}.".format(numero1, numero2))
else:
    print("{} não é múltiplo de {}.".format(numero1, numero2))