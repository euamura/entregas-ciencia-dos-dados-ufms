# importar biblioteca
import random

# criar lista original
lista_original = []

# preencher lista com números aleatório até 100
for _ in range(100):
    numero = random.randint(1, 100)
    lista_original.append(numero)

# criar listas secundárias
lista_pares = []
lista_impares = []

# separar listas
for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

# exibir

print("Lista matriz (100 números):")
print(lista_original)

print("\nLista de números pares:")
print(lista_pares)

print("\nLista de números ímpares:")
print(lista_impares)