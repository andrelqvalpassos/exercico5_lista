def processar_idade ():

    idades = []
    while True:
        idade = int(input(f"Digite sua idade ou - 1 para encerrar: "))
        if idade == -1:
            break
        idades.append(idade)
    qtd_idade = len(idades)
    print(f"A quantidade de idades e {qtd_idade}")

    print(f"Idades armazenada: {idades}")

    media_idade = sum(idades) / qtd_idade
    print(f"A media das idades e: {media_idade}")

    acima_media = [idade for idade in idades if idade > media_idade]
    print(f"Quantidade de idades acima da média: {len(acima_media)}")

    maior_idade = max(idades)
    menor_idade = min(idades)
    print(f"A maior idade e: {maior_idade}")
    print(f"A menor idade e: {menor_idade}")

    abaixo_18 = [idade for idade in idades if idade < 18]
    print(f"Quantidade de idades abaixo de 18 anos: {len(abaixo_18)}")






processar_idade()