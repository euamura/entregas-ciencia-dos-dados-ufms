# 🏦 Simulador de Conta Corrente

Implementação de uma **conta corrente bancária** em Java utilizando **Programação Orientada a Objetos (POO)**, com operações de depósito, saque com cheque especial, rendimento sobre saldo e exibição de dados.

---

## 🎯 Objetivo

Aplicar os fundamentos de **POO em Java**: definição de classes, atributos de instância, métodos de comportamento e o método `main` como ponto de entrada do programa.

---

## ⚙️ Funcionalidades

| Método | Descrição |
|---|---|
| `deposito(float valor)` | Adiciona valor ao saldo |
| `saque(float valor)` | Subtrai valor do saldo, respeitando o limite do cheque especial |
| `rendimento()` | Aplica juros de 1% sobre o saldo (somente se saldo ≥ 0) |
| `exibirSaldo()` | Imprime o saldo atual no console |
| `getNome()` | Retorna o nome completo do titular |
| `getNumero()` | Retorna o número da conta |

---

## 🧠 Conceitos aplicados

- **Classe e instância:** `ContaCorrente` como molde; `conta` como objeto criado com `new`.
- **Atributos de instância:** `saldo`, `juros`, `limiteChequeEspecial`, `nome`, `sobrenome`, `numero`.
- **Encapsulamento parcial:** métodos `public` com atributos package-private, discutindo visibilidade.
- **Cheque especial:** o saque só é efetuado se `(saldo - valor) >= limiteChequeEspecial` (limite padrão: R$ -200).
- **Rendimento condicional:** juros aplicados apenas quando `saldo >= 0`, evitando acúmulo de juros sobre dívida.

---

## 🗂️ Estrutura do código

```
simulador-conta-corrente/
├── ContaCorrente.java   # Código-fonte principal
└── README.md
```

### Atributos da classe

| Atributo | Tipo | Valor padrão | Descrição |
|---|---|---|---|
| `juros` | `float` | `0.01` | Taxa de rendimento (1%) |
| `saldo` | `float` | `0.0` | Saldo atual da conta |
| `limiteChequeEspecial` | `float` | `-200.0` | Limite mínimo permitido |
| `nome` | `String` | — | Primeiro nome do titular |
| `sobrenome` | `String` | — | Sobrenome do titular |
| `numero` | `long` | — | Número da conta |

### Fluxo do `main` (demonstração)

```
deposito(100)  → saldo = 100.00
saque(125)     → saldo = -25.00  (dentro do limite de -200)
rendimento()   → saldo não muda  (saldo < 0, juros não aplicados)
exibirSaldo()  → "Saldo atual: R$-25.0"
```

---

## ▶️ Como executar

> Requer JDK 8+ instalado.

```bash
# Compilar
javac ContaCorrente.java

# Executar
java ContaCorrente
```

---

## 💡 Saída esperada

```
Saldo atual: R$-25.0
```

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Programação Orientada a Objetos |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2026 |
