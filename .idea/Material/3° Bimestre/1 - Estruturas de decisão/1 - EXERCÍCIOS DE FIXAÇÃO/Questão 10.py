QTD_METROS_POR_LITROS = 54
PRECO_LATA = 80
metros = int(input("Digite os metros: "))
qtd_latas = metros//QTD_METROS_POR_LITROS
if metros % QTD_METROS_POR_LITROS != 0:
    qtd_latas += 1
preco_total = qtd_latas * PRECO_LATA
print("Qtd de latas: ", qtd_latas)
print("Preco total: ", preco_total)