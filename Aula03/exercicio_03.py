# entrada = input("Digite um numero para ver a tabuada: ")
# if entrada.isdigit():
#     numero = int(entrada)
# else:
#     numero = -1

# if numero >= 0:

#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# else:
#     print("Numero inválido, tente novamente.")


while True:
    print("\n==== MENU =====")
    print("1 - Par ou Ímpar")
    print("2 - Tabuada")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite um número: "))
    
        if numero % 2 == 0:
            print("O número é PAR")
        else:
            print("O número é IMPAR")
    elif opcao == "2":
        numero = int(input("Digite um número para ver tabuada: "))
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    elif opcao == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente Novamente.")

