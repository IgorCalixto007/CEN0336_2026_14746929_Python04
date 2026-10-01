import sys

#indice inicia em 0, porem o valor 0 é o nome do programa, entao utliza-se os indices 1 e 2, neste caso, 3 e 10
n1 = int(3)
n2 = int(10)

#necessario somar mais 1 para incluir o número 10 no resultado
for i in range(n1,n2+1):
    #imprime apenas impar
    if i%2 != 0:
        print(i)
