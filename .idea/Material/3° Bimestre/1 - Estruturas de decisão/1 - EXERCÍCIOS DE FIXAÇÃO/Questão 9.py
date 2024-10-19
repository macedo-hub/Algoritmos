hipotenusa = float(input("Digite o valor da hipotenusa: "))
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))
if (hipotenusa ** 2 == cateto1 ** 2 + cateto2 ** 2):
    print("É um triângulo retângulo!")
else:
    print("Não é um triângulo retângulo!")