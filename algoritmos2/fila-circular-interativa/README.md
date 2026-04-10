# 🔄 Fila Circular Interativa

Implementação de uma **fila circular** (circular buffer) com tamanho fixo, controlada por um **menu interativo** em linha de comando.

---

## 🎯 Objetivo

Praticar a estrutura de dados **fila** utilizando um array de tamanho fixo com comportamento circular, garantindo que a memória seja reutilizada de forma eficiente sem deslocar os elementos.

---

## ⚙️ Funcionalidades

| Opção | Operação | Descrição |
|---|---|---|
| `1` | Enfileirar | Insere um elemento no final da fila |
| `2` | Desenfileirar | Remove o elemento do início da fila |
| `3` | Consultar primeiro | Exibe o elemento na frente da fila sem removê-lo |
| `4` | Contar elementos | Mostra quantos elementos estão na fila |
| `5` | Imprimir fila | Lista todos os elementos em ordem |
| `0` | Sair | Encerra o programa |

---

## 🧠 Conceitos aplicados

- **Fila (Queue):** estrutura FIFO — o primeiro elemento a entrar é o primeiro a sair.
- **Circular buffer:** os ponteiros `inicio` e `fim` avançam usando o operador módulo (`%`), permitindo que o array seja reutilizado ciclicamente.
- **Controle de capacidade:** a fila detecta quando está cheia (`quantidade == tamanho`) e quando está vazia (`quantidade == 0`), emitindo mensagens de erro adequadas.

---

## 🗂️ Estrutura do código

```
fila-circular-interativa/
├── fila_circular_interativa.py   # Código-fonte principal
└── README.md
```

### Classe `Fila`

| Atributo/Método | Descrição |
|---|---|
| `tamanho` | Capacidade máxima da fila |
| `dados[]` | Array interno de armazenamento |
| `inicio` | Índice de remoção |
| `fim` | Índice de inserção |
| `quantidade` | Número atual de elementos |
| `enfileirar(elemento)` | Insere elemento (verifica capacidade) |
| `desenfileirar()` | Remove elemento (verifica vazio) |
| `consultar()` | Exibe o primeiro elemento |
| `contar()` | Exibe a contagem atual |
| `imprimir()` | Percorre e exibe todos os elementos |

---

## ▶️ Como executar

> Requer Python 3.x instalado.

```bash
python fila_circular_interativa.py
```

Ao iniciar, o programa solicita o **tamanho máximo** da fila e em seguida apresenta o menu.

---

## 💡 Exemplo de uso

```
Defina o tamanho máximo da fila: 3

=== MENU DA FILA ===
1 - Enfileirar
...

Escolha uma opção: 1
Digite o elemento a ser inserido: João
Elemento 'João' inserido na fila.

Escolha uma opção: 5
Fila atual: João
```

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Algoritmos II |
| **Módulo** | 3 |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2025 |
