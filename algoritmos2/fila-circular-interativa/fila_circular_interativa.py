class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho  # Array fixo
        self.inicio = 0  # Índice de remoção
        self.fim = 0     # Índice de inserção
        self.quantidade = 0  # Elementos atuais na fila

    def enfileirar(self, elemento):
        if self.quantidade < self.tamanho:
            self.dados[self.fim] = elemento
            self.fim = (self.fim + 1) % self.tamanho  # Garante que o índice rode no array
            self.quantidade += 1
            print(f"Elemento '{elemento}' inserido na fila.")
        else:
            print("Erro: Fila cheia!")

    def desenfileirar(self):
        if self.quantidade > 0:
            elemento = self.dados[self.inicio]
            self.dados[self.inicio] = None  # Opcional: limpar posição
            self.inicio = (self.inicio + 1) % self.tamanho
            self.quantidade -= 1
            print(f"Elemento '{elemento}' removido da fila.")
        else:
            print("Erro: Fila vazia!")

    def consultar(self):
        if self.quantidade > 0:
            print(f"O primeiro elemento da fila é: '{self.dados[self.inicio]}'")
        else:
            print("A fila está vazia!")

    def contar(self):
        print(f"A fila contém {self.quantidade} elemento(s).")

    def imprimir(self):
        if self.quantidade == 0:
            print("Fila vazia.")
        else:
            print("Fila atual:", end=" ")
            i = self.inicio
            for _ in range(self.quantidade):
                print(self.dados[i], end=" ")
                i = (i + 1) % self.tamanho
            print()


def menu():
    tamanho = int(input("Defina o tamanho máximo da fila: "))
    fila = Fila(tamanho)

    while True:
        print("\n=== MENU DA FILA ===")
        print("1 - Enfileirar")
        print("2 - Desenfileirar")
        print("3 - Consultar primeiro")
        print("4 - Contar elementos")
        print("5 - Imprimir fila")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            elemento = input("Digite o elemento a ser inserido: ")
            fila.enfileirar(elemento)
        elif opcao == '2':
            fila.desenfileirar()
        elif opcao == '3':
            fila.consultar()
        elif opcao == '4':
            fila.contar()
        elif opcao == '5':
            fila.imprimir()
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
