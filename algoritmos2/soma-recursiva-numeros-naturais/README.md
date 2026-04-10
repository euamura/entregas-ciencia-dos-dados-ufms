# ➕ Soma Recursiva de Números Naturais

Programa que calcula a **soma dos N primeiros números naturais** utilizando **recursão**, com validação da entrada do usuário.

---

## 🎯 Objetivo

Praticar o conceito de **funções recursivas** em Python, compreendendo o caso base e o caso recursivo, além de aplicar validação de entrada para garantir que o dado fornecido seja um número natural (inteiro não-negativo).

---

## ⚙️ O que o programa faz

1. Solicita ao usuário um número natural `n`.
2. Valida se o número é não-negativo.
3. Calcula recursivamente a soma `1 + 2 + 3 + ... + n`.
4. Exibe o resultado.

---

## 🧠 Conceitos aplicados

- **Recursão:** a função chama a si mesma com um argumento reduzido até atingir o caso base (`n == 0`).
- **Caso base:** `soma_num_recursivo(0)` retorna `0`, interrompendo a recursão.
- **Caso recursivo:** `soma_num_recursivo(n)` retorna `n + soma_num_recursivo(n - 1)`.
- **Validação de entrada:** o programa rejeita números negativos com uma mensagem orientativa.

---

## 🗂️ Estrutura do código

```
soma-recursiva-numeros-naturais/
├── soma_recursiva_numeros_naturais.py   # Código-fonte principal
└── README.md
```

### Função principal

```python
def soma_num_recursivo(n):
    if n == 0:
        return 0
    else:
        return n + soma_num_recursivo(n - 1)
```

### Árvore de chamadas para `n = 4`

```
soma(4)
└── 4 + soma(3)
         └── 3 + soma(2)
                  └── 2 + soma(1)
                           └── 1 + soma(0)
                                    └── 0
Resultado: 4 + 3 + 2 + 1 + 0 = 10
```

---

## ▶️ Como executar

> Requer Python 3.x instalado.

```bash
python soma_recursiva_numeros_naturais.py
```

---

## 💡 Exemplo de uso

```
Digite um número natural (inteiro e positivo): 5
A soma dos 5 primeiros números naturais é: 15
```

```
Digite um número natural (inteiro e positivo): -3
Por favor, digite um número natural (inteiro e positivo).
```

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Algoritmos II |
| **Módulo** | 4 |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2025 |
