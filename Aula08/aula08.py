"""
dicionario {} -> Para acessar dados usamos o nome chave
listas [] -> Para acessar dados usamos a posição da lista
"""

notas = [10, 8, 5, 10, True, 7, "André"]
#         0  1  2   3    4   5     6

# append() — adiciona um item ao final
notas.append("SENAC") 
print(notas)

# insert() — insere item em posição específica
print(notas)
notas.insert(0, False) 

# extend() — adiciona vários itens
nova_lista.extend(notas)
nova_lista = ["Olá mundo", 1980, 24.7] 
print(nova_lista)

# remove() — remove pelo valor
notas.remove(10)   
print(notas)
notas.remove(True)
print(notas)
notas.remove("SENAC")
print(notas)   
notas.remove("andré") 
# O método remove o Case sensitive 

#  pop() — remove pelo índice (ou último)
nomes_numeros = ["Adenilson", 19, "Anna", 45, "Iara", 390] 
# POP
nomes_numeros.pop()
print(nomes_numeros) 

# clear() — limpa toda a lista
# CLEAR
print(nomes_numeros.clear()) 
# INDEX
print(nomes_numeros.index(390))
print(nomes_numeros)

# count() — conta ocorrências
print(nomes_numeros.count(390)) 

numeros = [34, 35, 67, 89, 43, 26, 58, 66, 33, 90]
numeros.sort()
print(numeros)

# REVERSE
numeros.reverse()
print(numeros)

# sort() — ordena a lista
nome = ["Adenilson", "Anna", "Beatriz", "Anne", "Bianca"] 
# nome.sort()
# print(nome)
nome.reverse()
print(nome)