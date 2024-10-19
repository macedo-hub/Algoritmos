idade = int(input("Digite a sua idade: "))
if (idade < 12):
    print("Você é criança.")
elif (idade >= 12 and idade < 18):
    print("Você é jovem.")
elif (idade >= 18 and idade < 60):
    print("Você é adulto.")
else:
    print("Você é idoso.")