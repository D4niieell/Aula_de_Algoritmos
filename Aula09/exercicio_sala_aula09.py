# O professor digita 5 notas
# Crie uma função que receba 5 notas de um aluno que calcule e retorne a média.
def receber_notas():
    notas = []
    for i in range(5):
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas_aluno = receber_notas()
media_final = calcular_media(notas_aluno)

print(f"Média do aluno: {media_final:.2f}")

# Crie uma função para receber a média do aluno e retorne se ele está aprovado ou reprovado.
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
media_aluno = float(input("Digite a média do aluno: "))
resultado = verificar_aprovacao(media_aluno)

print("Resultado:", resultado)