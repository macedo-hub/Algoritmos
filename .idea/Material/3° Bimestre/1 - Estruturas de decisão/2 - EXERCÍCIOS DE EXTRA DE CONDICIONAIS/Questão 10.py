ano = int(input("Digite um ano(aaaa): "))
if (ano % 4 == 0 and ano % 100 !=0 ) or (ano % 400 == 0):
    print(ano,"é um ano bissexto.")
else:
print(ano,"não é um ano bissexto.")
