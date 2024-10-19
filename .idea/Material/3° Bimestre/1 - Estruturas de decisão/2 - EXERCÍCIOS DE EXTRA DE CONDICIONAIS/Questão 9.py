n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
op = input("Digite uma operação aritmética: ")
resposta = 0
if (op == "+"):
    resposta= n1 + n2
elif (op == "-"):
resposta = n1 - n2
elif (op == "*"):
resposta = n1 * n2
else:
resposta = n1 / n2
print(round(resposta,4))
