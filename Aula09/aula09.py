# Em Python usamos a palavra-chave def

# Parametros sempre vão dentro do parenteses
def saudacao(nome):
    print("Olá, ", nome ," seja bem-vindo") 
# chamar uma função
saudacao("Daniel")

# Funções podem retornar valores usando return.
# recebe dois valores, faz a soma e retorna o resultado 
def soma(valor1, valor2):
    return valor1 + valor2

salario_funcionario = 1600
beneficio = 200
novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

# soma dois valores se a idade do usuario for igual ou maior de 18
# Se não mostrar mensagem "Sua idade é menor que 18" 
idade_usuario = int(input("Digite sua idade: "))
if idade_usuario >= 18:
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o segundo valor: "))
    resultado = soma(var1, var2) 
    print(resultado)
else:
    print("Sua idade é menor que 18")

# Retorna a quantidade de itens.
# Também funciona com strings:
lista = [20, 1, 6, 10, 45]
palavra = "Ano"

# Retornar a quantidade de informações contidas em uma variavel
print(len(lista))
print(len(palavra))

# SUM - soma toda a minha lista numerica
print(sum(lista))

# max() — Maior valor
print("Maior ", max(lista))

# min() — Menor valor
print("Menor ", min(lista))

# sorted() — Ordenar
print(sorted(lista))

# type() — Descobrir o tipo
tipo = input("Digite um numero: ")
print(type(tipo))

# Coverter o tipo
print(float(tipo))
print(int(tipo))