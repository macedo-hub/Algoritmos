valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalho no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - descontos
print("Seu salário bruto nesse mês foi R$ {:.2f}".format(salario_bruto))
print("Seu desconto de imposto de renda nesse mês foi R$
{:.2f}".format(imposto_de_renda))
print("Seu desconto de INSS nesse mÊs foi R$ {:.2f}".format(inss))
print("Seu desconto de sindicato nesse mês foi R$ {:.2f}".format(sindicato))
print("O total descontado nesse nesse mês foi R$ {:.2f}".format(descontos))
print("O seu salário líquido nesse mês foi R$ {:.2f}".format(salario_liquido))