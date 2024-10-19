tipo_combustivel = input("Digite o tipo de combustível (gasolina ou álcool): ").strip().lower()
litros = float(input("Digite a quantidade de litros que deseja abastecer: "))

preco_gasolina = 6.99
preco_alcool = 4.99

if tipo_combustivel == "gasolina":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_total = litros * preco_gasolina * (1 - desconto)

elif tipo_combustivel == "álcool":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_total = litros * preco_alcool * (1 - desconto)

else:
    valor_total = 0
    print("Tipo de combustível inválido.")

if valor_total > 0:
    print("O valor total a pagar pelo abastecimento é: R$ {:.2f}".format(valor_total))
