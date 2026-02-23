nome = input("Digite o seu nome: ")
print("Seu nome é: ", nome)

# # int = inteiros
# # float = decimais

numeros = int(input("Digite um numeros de 1 a 10: "))
soma = numeros + 10 
input(soma)

calculo_salario = float(input("Digite o seu salario: "))
soma_salario = calculo_salario * 3.5
print(soma_salario)

idade = 16

if idade >= 18: # True
     print("Sua idade é: ", idade) # Identação

# IF - ELSE
valida_idade = int(input("Digite sua idade: "))

# CONDICIONAL TERMINÁRIO
status = "menor de idade" if valida_idade < 18 else "maior de idade"
print(status)

if valida_idade < 18: # false
    input("Você é menor de idade e precisa da presença dos pais")
else:
    print("Você é o maior de idade, pode entrar!")

# IF - ELIF - ELSE
nota = int(input("Digite a nota do aluno: "))
nome_aluno = input("Digite o nome do aluno: ")

if nota >= 9:
     print(f"O aluno {nome_aluno} está Aprovado com a nota {nota}")
elif nota >= 7 and nota <= 8:
     print(f"O aluno {nome_aluno} está Aprovado por conselho com a nota {nota}")
else:
     print(f"O aluno {nome_aluno} está Reprovado com a nota {nota}")


# Se o usuario for menor de idade então ele precisa ter autorização
# Se o usuario for menor de idade então ele precisa ter a altura minima
idade_cliente = int(input("Digite a idade do cliente: "))
altura_cliente = float(input("Digite a altura do cliente: "))

if idade_cliente < 18:
     print("O cliente é menor de idade e não pode entrar no brinquedo")
else: 
     if altura_cliente >= 1.50:
         print("Você é maior de idade e tem a altura minima para o brinquedo")
     else:
         print("Você mesmo sendo maior de idade tem menos de 1.50 de altura e não pode ir ao brinquedo")
         print("Cliente maior de idade pode subir no brinquedo")