# Criar um dicionário com dados digitados pelo usuário.
# Peça ao usuário:
# nome
# idade
# cidade
# Guarde em um dicionário e mostre na tela.

usuario = {
    
    "nome": " ",
    "idade": " ",
    "cidade": " "
}

usuario["nome"] = input("Digite o seu nome: ")

usuario["idade"] = input("Digite sua idade: ")

usuario["cidade"] = input("Digite o nome de sua cidade: ")

for valor in usuario.items():
    print(valor)

for chave, valor in usuario.items():
    print(chave, ":", valor)
