#criando a lista
lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#compreensao de lista que cria uma lista de tuplas se baseando no comprimento de cada string
listax = []
for dna in lista:
    listax.append(len(dna))
    listax.append(dna)

#lista_tuple = [tuple(dnalen) for dnalen in dnalen_list]
print(listax)
