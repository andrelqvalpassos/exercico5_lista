def vendido_vendedor ():
    
    num_vendedores = int(input("Digite o número total de vendedores: "))

    valor_vendido = []
    
    vendedor = []

    for i in range(num_vendedores):
        nome = str(input(f"Digite seu nome {i + 1}: "))
        vendedor.append(nome)

        valor = float(input(f"Digite o valor vendido pelo vendedor {nome} no ano: "))
        valor_vendido.append(valor)

        maior_valor_vendido = max(valor_vendido)
        menor_valor_vendido = min(valor_vendido)

        indice_maior = valor_vendido.index(maior_valor_vendido)
        indice_menor = valor_vendido.index(menor_valor_vendido)

        print("\nVendedores e seus totais de vendas:")
    for i in range(num_vendedores):
        print(f"{vendedor[i]}: R${valor_vendido[i]:.2f}")

    # Destaque para o vendedor com maior e menor volume de vendas
    print(f"\nVendedor com maior volume de vendas: {vendedor[indice_maior]} - R${maior_valor_vendido:.2f}")
    print(f"Vendedor com menor volume de vendas: {vendedor[indice_menor]} - R${menor_valor_vendido:.2f}")

vendido_vendedor()