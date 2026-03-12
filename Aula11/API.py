# API
# Introdução a APIs em Python

import requests

URL = "https://rickandmortyapi.com/api/character"

resposta = requests.get(URL) # retorno status 200

json = resposta.json() # retornar o JSON
print(json)

personagem = json["results"] # Consulta os meus personagens

print(personagem)
# laço de repetição para consulyat apenas os nomes dos personagens
for nome_personagem in personagem:
    print(nome_personagem["name"]) 

# Retornar mais informações além do nome
for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especie: ", mais_info["species"])
    print("----------------------------------")

# Pedir ao usuario para digitar um ID e retornar da API o personagem referentea esse ID
id = int(input("Digite um numero inteiro: "))
link_API = f"https://rickandmortyapi.com/api/character/{id}"
resposta = requests.get(link_API)
novo_json = resposta.json()
print("Nome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especie: ", novo_json["species"])
print("----------------------------------")