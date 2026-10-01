lista = [101,2,15,22,95,33,2,27,72,15,52]
par = 0
impar = 0

#transformando a lista num iteravel e ordenando em ordem crescente
for n in sorted(iter(lista)):
    print(n)
    if n%2 == 0:
        par += n
    else:
        impar += n

#imprimindo a soma dos valores pares e impares separadamente
print("Soma dos números pares: "+ str(par))
print("Soma dos números ímpares: "+ str(impar))
