#variaveis para o fatorial e o contador
contagem = 1
fatorial = 1

#definindo até que numero vai o contador
while contagem <= 1000:
    fatorial *= contagem
    contagem += 1

#impriminto o fatorial
print(fatorial)
