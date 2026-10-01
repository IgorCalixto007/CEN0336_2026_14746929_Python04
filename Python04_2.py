#string
taxa = "sapiens, erectus, neanderthalensis"

#imprimindo a string
print(taxa)

#imprimindo o segundo caractere da string
print(taxa[1])

#imprimindo o tipo da variavel
print(type(taxa))

#convertendo a string em uma lista, elementos separados por virgula
species = taxa.split(", ")

#imprimindo a lista
print(species)

#imprimindo o segundo elemento da lista
print(species[1])

#imprimindo o tipo da variavel
print(type(species))

#imprimindo a lista ordenada em ordem alfabetica
print(sorted(species))

#definindo que o fator determinante da ordenação da lista é o comprimento
print(sorted(species, key=len))
