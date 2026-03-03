"""
Crie uma lista com 4 nomes
Peça ao usuário um nome para remover
Se o nome existir, remova
Mostre a lista final
"""

nomes = ["Ana", "Carlos", "Mariana, João"]
print("Lista inicial:", nomes)
nome_remover = input("Digite um nome para remover: ")
if nome_remover in nomes:
    nomes.remove(nome_remover)
    print("Nome removido com sucesso!")
else:
    print("Nome não encontrado na lista.")
print("Lista final:", nomes)
