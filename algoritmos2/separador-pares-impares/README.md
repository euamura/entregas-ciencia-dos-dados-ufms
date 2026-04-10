# 🔢 Separador de Pares e Ímpares

Script que gera uma lista de **100 números aleatórios** e os separa automaticamente em duas sublistas: **números pares** e **números ímpares**.

---

## 🎯 Objetivo

Praticar a **manipulação de listas** em Python, a geração de dados aleatórios e a aplicação de lógica de filtragem com estruturas de repetição e condicionais.

---

## ⚙️ O que o programa faz

1. Gera uma lista com **100 números inteiros aleatórios** no intervalo de `1` a `100`.
2. Percorre a lista e classifica cada número:
   - **Par** → adicionado à `lista_pares`
   - **Ímpar** → adicionado à `lista_impares`
3. Exibe as três listas no terminal.

---

## 🧠 Conceitos aplicados

- **`random.randint(a, b)`** — geração de inteiros aleatórios no intervalo `[a, b]`.
- **Operador módulo `%`** — verificação de paridade (`numero % 2 == 0`).
- **Listas (`list`)** — criação e manipulação com `append()`.
- **Laços `for`** — iteração sobre sequências.

---

## 🗂️ Estrutura do código

```
separador-pares-impares/
├── separador_pares_impares.py   # Código-fonte principal
└── README.md
```

### Fluxo do script

```
Gera lista_original (100 números aleatórios)
    │
    ▼
Para cada número em lista_original:
    ├── par?   → adiciona em lista_pares
    └── ímpar? → adiciona em lista_impares
    │
    ▼
Exibe lista_original, lista_pares e lista_impares
```

---

## ▶️ Como executar

> Requer Python 3.x instalado.

```bash
python separador_pares_impares.py
```

A saída é gerada automaticamente, sem necessidade de entrada do usuário.

---

## 💡 Exemplo de saída

```
Lista matriz (100 números):
[42, 17, 83, 56, ...]

Lista de números pares:
[42, 56, ...]

Lista de números ímpares:
[17, 83, ...]
```

> Os números variam a cada execução por serem gerados aleatoriamente.

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Algoritmos II |
| **Módulo** | 2 |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2025 |
