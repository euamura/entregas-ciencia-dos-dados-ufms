"""
Hortifruti

Objetivo: programa tem o objetivo de cadastrar a quantidade de itens dos produtos a ser armazenados, armazenar os produtos e preço, e criar uma input de busca.

"""
# Função para cadastrar produtos
def cadastrar_produtos():
  # Criar lista para armazenamento de produtos
    produtos = [] 

    n = int(input("Quantos produtos quer cadastrar? "))

    # Enquanto não tiver cadastrado n produtos
    while len(produtos) < n:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        # Verifica se já existe
        ja_existe = False
        for p in produtos:
          # Permitir input em maiúsculo ou minúsculo
            if p[0].lower() == nome.lower():
                ja_existe = True
                break

        if ja_existe:
            print("Produto já cadastrado")
        else:
            produtos.append([nome, preco])

    return produtos

# Função para buscar produtos
def buscar_produto(produtos):
    while True:
        nome = input("Digite o nome do produto para buscar (ou 'Fim' para encerrar): ")
        # Comando finaliza o programa
        ## Permitir input em maiúsculo ou minúsculo
        if nome.lower() == "fim":
            break
        # Busca, caso programa não seja encerrado
        encontrado = False
        for p in produtos:
            if p[0].lower() == nome.lower():
                print(f"{p[0]} custa R$ {p[1]:.2f}")
                encontrado = True
                break
        # Saída caso o produto não esteja cadastrado
        if not encontrado:
            print("Produto não cadastrado.")


# Programa principal

#Função para unir as defs de cadastro e busca
def main():
    lista = cadastrar_produtos()
    buscar_produto(lista)

# Executar programa principal
main()
