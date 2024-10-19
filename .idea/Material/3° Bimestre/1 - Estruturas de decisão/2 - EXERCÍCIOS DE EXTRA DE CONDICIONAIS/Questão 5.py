nota1 = int(input("Digite a 1ª nota: "))
nota2 = int(input("Digite a 2ª nota: "))
nota3 = int(input("Digite a 3ª nota: "))
media =(nota1+nota2+nota3)/3
print("A média foi:",round(media,3))
if (media>=90):
    print("Excelente.")
elif (media >= 80 and media <= 89.9):
print("Ótimo.")
elif (media >= 70 and media <= 79.9):
print("Bom.")
else:
print("Estude um pouco mais!.")