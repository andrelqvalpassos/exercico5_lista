# Lista para armazenar os 10 números
numeros = []

# Solicitar 10 números
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Separar os números pares e ímpares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Imprimir os números pares e ímpares
print("\nLista de numeros: ", numeros)
print("\nNúmeros pares:", pares)
print("Números ímpares:", impares)
