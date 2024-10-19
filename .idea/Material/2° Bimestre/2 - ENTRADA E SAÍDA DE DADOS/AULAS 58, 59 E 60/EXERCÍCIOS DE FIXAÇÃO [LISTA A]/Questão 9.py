nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (metros): "))
imc = peso / altura ** 2
print("O IMC de {} é {:.2f}".format(nome, imc))
