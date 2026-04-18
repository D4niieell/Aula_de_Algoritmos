# Comparação de valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    print("valor1 é maior que valor2 ")
elif valor1 < valor2:
    print("valor2 é maior que valor1")    
else:
    print("valor2 é maior que valor1 ")

# Verificação de mês
mes = int(input("Digite um numero de mes (1-12): "))

if 1 <= mes <= 12:
    print(f"Mês válido: {mes}")
else:
    print("Mês inválido! Digite um número entre 1 e 12.")

