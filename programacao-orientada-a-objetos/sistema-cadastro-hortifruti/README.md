# 🥦 Sistema de Cadastro de Hortifruti

Sistema em Python para **cadastrar produtos e preços** de um hortifruti e permitir a **busca por nome**, com tratamento de duplicatas e entrada insensível a maiúsculas/minúsculas.

---

## 🎯 Objetivo

Praticar a **modularização de código** com funções, manipulação de listas de listas e interação com o usuário via terminal, simulando um pequeno sistema de gestão de estoque.

---

## ⚙️ Funcionalidades

- **Cadastro de produtos:** o usuário define quantos produtos deseja cadastrar, informa nome e preço de cada um.
- **Validação de duplicatas:** o sistema impede o cadastro de um produto já existente (comparação case-insensitive).
- **Busca de produtos:** após o cadastro, o usuário pode pesquisar produtos pelo nome. O programa exibe o preço formatado ou informa que o produto não está cadastrado.
- **Encerramento:** digitar `fim` (em qualquer capitalização) encerra a busca.

---

## 🧠 Conceitos aplicados

- **Funções (`def`)** — separação clara das responsabilidades: `cadastrar_produtos()` e `buscar_produto()`.
- **Listas de listas** — cada produto é armazenado como `[nome, preco]` dentro de uma lista principal.
- **Comparação case-insensitive** — uso de `.lower()` para normalizar entradas.
- **Laços `while` e `for`** — controle de fluxo para cadastro e busca.
- **Formatação de strings** — exibição de preço com `:.2f` (duas casas decimais).

---

## 🗂️ Estrutura do código

```
sistema-cadastro-hortifruti/
├── sistema_cadastro_hortifruti.py   # Código-fonte principal
└── README.md
```

### Funções

| Função | Descrição |
|---|---|
| `cadastrar_produtos()` | Lê N produtos do usuário, evita duplicatas, retorna a lista |
| `buscar_produto(produtos)` | Loop de busca por nome até o usuário digitar "fim" |
| `main()` | Orquestra o fluxo: cadastro → busca |

---

## ▶️ Como executar

> Requer Python 3.x instalado.

```bash
python sistema_cadastro_hortifruti.py
```

---

## 💡 Exemplo de uso

```
Quantos produtos quer cadastrar? 2
Digite o nome do produto: Banana
Digite o preço do produto: 3.50
Digite o nome do produto: Maçã
Digite o preço do produto: 7.90

Digite o nome do produto para buscar (ou 'Fim' para encerrar): banana
Banana custa R$ 3.50

Digite o nome do produto para buscar (ou 'Fim' para encerrar): uva
Produto não cadastrado.

Digite o nome do produto para buscar (ou 'Fim' para encerrar): Fim
```

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Programação Orientada a Objetos / Algoritmos I |
| **Módulo** | 5 |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2025 |
