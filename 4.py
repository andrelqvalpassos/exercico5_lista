def temperaturas_anuais():
    # Lista com o nome dos meses por extenso
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    # Lista para armazenar as temperaturas médias de cada mês
    temperaturas = []

    # Solicita ao usuário a temperatura média de cada mês
    for i in range(12):
        temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
        temperaturas.append(temp)

    # Calcula a média anual de temperaturas
    media_anual = sum(temperaturas) / 12

    # Exibe a média anual
    print(f"\nMédia anual de temperaturas: {media_anual:.2f}°C")

    # Exibe os meses com temperaturas acima da média anual
    print("\nMeses com temperaturas acima da média anual:")
    for i in range(12):
        if temperaturas[i] > media_anual:
            print(f"{meses[i]}: {temperaturas[i]:.2f}°C")

# Chama a função para executar o programa
temperaturas_anuais()
