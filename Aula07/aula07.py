# Dicionário em Python
aluno = {
    # chave : valor
    "nome": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "TÉCNICO EM INFORMÁTICA PARA INTERNET",

    # Array
    "Array": [30, True, "Texto"],
    
    # Dicionário dentro de outro dicionário
    "endereco": {
        "cidade": "São Paulo",
        "estado": "SP",
        "numero": 234
    }
}

# retorna nome do aluno
print(aluno["nome"]) 

# retorna o array
print(aluno["Array"])

# retorna o endereço, estamos acessando um dicionário 
print(aluno["endereco"])

# acessar apenas um único dado do endereco
print(aluno["endereco"]["estado"])

# acessando campo específiico dentro de um Array
print(aluno["Array"][1]) 

# ALTERAR DADOS DO DICIONÁRIO
aluno["idade"] = 20
print(aluno["idade"])

# Alterar dados dentro de um array que está dentro do dicionário
aluno["Array"][2] = 9
print(aluno["Array"][2])

# Alterar dados do dicionário endereço que está dentro do dicionário aluno
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"])
print(aluno["endereco"]["cidade"])

# Adicionar um novo campo
aluno["periodo"] = "Noturno"
print(aluno)

# Deletar uma informação
del aluno["idade"], 

# deletar mais de uma informação na mesma linha
del aluno["endereco"], aluno["curso"]
print(aluno)

# Percorrer um dicionário usando laço de repetição
for chave in aluno:
    print(chave)

# Percorrer um dicionário usando laço de repetição para retornar os valores
for valor in aluno.values():
    print(valor)

# Percorrer um dicionário e retornar chave e valor
for chave, valor in aluno.items():
    print(chave, ":", valor)