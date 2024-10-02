medias = []

for i in range (1, 6): #percorre de 1 a 5
    print(f"Estudante {i}: ")
    
    nota1 = float(input("Digite sua primera nota: "))
    nota2 = float(input("Digite sua segunda nota: "))

    media = (nota1 + nota2) / 2
    medias.append(media)

print("\nLista das medias: ")
print(medias)

#verifica se estudante e aprovado
estudante_aprovado = sum(1 for media in medias if media >= 7)

print(f"Os alunos aprovados são: {estudante_aprovado}")