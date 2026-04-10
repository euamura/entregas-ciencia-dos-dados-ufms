# chekout_algoritmos2_mod4.py

## função recursiva soma numeros naturais
def soma_num_recursivo(n):
    if n ==0:
        return 0
    else:
        return n + soma_num_recursivo(n-1)
    
## entrada
numero = int(input("Digite um número natural (inteiro e positivo): "))
### validação
if numero < 0:
    print("Por favor, digite um número natural (inteiro e positivo).")
else:
    resultado = soma_num_recursivo(numero)
    print(f"A soma dos {numero} primeiros números naturais é: {resultado}")