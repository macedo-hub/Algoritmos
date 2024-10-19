tamanho_do_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))
# Converte Megabit por segundos em Megabyte por segundo
velocidade_mbs = velocidade_mbps / 8
# Calcula o tempo de download em segundos
tempo_segundos = tamanho_do_arquivo_mb / velocidade_mbs
# Converte segundo em minutos
tempo_minutos = tempo_segundos / 60
print("O tempo aproximado de download em minutos é {:.2f}".format(tempo_minutos))
