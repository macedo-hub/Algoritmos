PORCENTAGEM = 20
preco_total = 1000.0
deconto = preco_total * (PORCENTAGEM / 100)
novo_preco = preco_total - deconto
print("Após", PORCENTAGEM, "% de desconto sobre R$", preco_total, "o novo preço é R$", novo_preco)
