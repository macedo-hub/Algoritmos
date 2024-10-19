nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segundo nota: "))
nota3 = float(input("Digite a segundo nota: "))
media = (nota1 + nota2 + nota3) / 3
if (media < 4.0):
    print("Sua média é {}, então você está reprovado.".format(media))
elif (media >= 4.0 and media < 7.0):
    print("Sua média é {}, então você precisa fazer final.".format(media))
else:
    print("Sua média é {}, então você está aprovado.".format(media))
