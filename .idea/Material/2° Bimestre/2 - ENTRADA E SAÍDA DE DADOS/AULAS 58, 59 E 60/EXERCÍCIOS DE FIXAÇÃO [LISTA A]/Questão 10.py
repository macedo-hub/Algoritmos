nome = input("Digite o nome do(a) aluno(a): ")
nota1 = float((input("Digite a primeira nota de {}: ".format(nome))))
nota2 = float((input("Digite a segunda nota de {}: ".format(nome))))
soma = nota1 + nota2
media = soma / 2
print("A média aritmética de {} é: {:.1f}".format(nome, media))
