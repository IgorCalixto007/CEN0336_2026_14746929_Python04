#criando a lista
lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#percorre a lista usando enumerate para obter o índice e o DNA simultaneamente
for index, dna in enumerate(lista):
    #imprimindo o índice, o tamanho da string e a sequência
    print(index, len(dna), dna, sep='\t')
