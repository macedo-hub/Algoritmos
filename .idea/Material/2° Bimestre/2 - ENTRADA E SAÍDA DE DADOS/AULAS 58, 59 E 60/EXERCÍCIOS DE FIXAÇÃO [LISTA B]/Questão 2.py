principal = float(input("Digite o valor principal: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
tempo = int(input("Digite o tempo de aplicação em meses: "))
taxa_convertida = taxa / 100
juros = principal * taxa_convertida * tempo
montante = principal + juros
print("Juros acumulados: R$ {:.2f}".format(juros))
print("Montante: R$ {:.2f}".format(montante))