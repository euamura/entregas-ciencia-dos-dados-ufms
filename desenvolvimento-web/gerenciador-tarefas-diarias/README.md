# 🗓️ Gerenciador de Tarefas Diárias

Aplicação web para **cadastrar, organizar e acompanhar tarefas diárias**, construída com **Vue.js 2** e **Bootstrap 5**, com persistência automática no **LocalStorage** do navegador.

---

## 🎯 Objetivo

Aplicar os fundamentos de **desenvolvimento web** aprendidos na disciplina, utilizando o framework Vue.js para manipulação reativa de dados e o Bootstrap para criação de uma interface responsiva e funcional.

---

## ⚙️ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| ➕ Adicionar tarefa | Cadastro com identificação, descrição e data/hora |
| ✅ Concluir tarefa | Marca a tarefa como concluída (destaque visual em verde) |
| 🔁 Reabrir tarefa | Reverte uma tarefa concluída para pendente |
| ❌ Excluir tarefa | Remove a tarefa da lista permanentemente |
| 🔍 Filtrar tarefas | Exibe todas, apenas pendentes ou apenas concluídas |
| 💾 Persistência | Tarefas salvas automaticamente no LocalStorage |
| 🕒 Formatação de data | Datas exibidas no padrão brasileiro (`dd/mm/aaaa hh:mm`) |

---

## 🧠 Conceitos aplicados

- **Vue.js 2 (Options API):**
  - `data()` — estado reativo da aplicação (lista de tarefas, campos do formulário, filtro ativo).
  - `computed` — propriedade `tarefasFiltradas` que recalcula automaticamente conforme o filtro selecionado.
  - `methods` — funções de CRUD das tarefas e integração com LocalStorage.
  - `mounted()` — carrega dados salvos ao iniciar a aplicação.
  - Diretivas: `v-model`, `v-for`, `v-if`, `v-on` / `@click`.
- **Bootstrap 5** — layout responsivo com `container`, `list-group`, `btn` e `form-control`.
- **LocalStorage** — persistência client-side via `JSON.stringify` / `JSON.parse`.
- **`toLocaleString('pt-BR')`** — formatação de data e hora conforme padrão brasileiro.

---

## 🗂️ Estrutura do projeto

```
gerenciador-tarefas-diarias/
├── index.html   # Aplicação completa (HTML + Vue.js inline)
└── README.md
```

> Todo o código está contido em um único arquivo HTML — não são necessários servidor ou dependências instaladas localmente.

### Estrutura da instância Vue

| Seção | Responsabilidade |
|---|---|
| `data()` | Armazena `tarefas[]`, `idTarefa`, `descricao`, `dataHora`, `filtro` |
| `computed.tarefasFiltradas` | Filtra a lista conforme o valor de `filtro` |
| `methods.addTarefa()` | Valida campos e adiciona nova tarefa |
| `methods.concluirTarefa()` | Define `concluida = true` |
| `methods.reabrirTarefa()` | Define `concluida = false` |
| `methods.removeTarefa()` | Remove tarefa pelo índice |
| `methods.salvarLocalStorage()` | Serializa e salva no navegador |
| `methods.carregarLocalStorage()` | Restaura tarefas salvas ao iniciar |
| `mounted()` | Chama `carregarLocalStorage()` na inicialização |

---

## 🧩 Tecnologias utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| HTML5 | — | Estrutura da página |
| Bootstrap | 5.3.6 | Estilização e responsividade |
| Vue.js | 2.x | Reatividade e lógica da aplicação |
| LocalStorage | API Web nativa | Persistência dos dados no navegador |

---

## ▶️ Como executar

Não é necessário instalar dependências nem configurar um servidor.

1. Faça o download ou clone este repositório.
2. Abra o arquivo `index.html` diretamente em qualquer navegador moderno.

```bash
# Opcional: clonar o repositório
git clone https://github.com/seuusuario/entregas-ciencia-dos-dados-ufms.git

# Navegar até a pasta
cd entregas-ciencia-dos-dados-ufms/desenvolvimento-web/gerenciador-tarefas-diarias

# Abrir no navegador (Linux/Mac)
xdg-open index.html
```

---

## 💡 Como usar

1. Preencha a **identificação**, a **descrição** e a **data/hora** da tarefa.
2. Clique em **"Adicionar Tarefa"**.
3. Use os botões **"Concluir"**, **"Reabrir"** ou **"Excluir"** em cada tarefa.
4. Utilize o **seletor de filtro** para visualizar todas, pendentes ou concluídas.
5. As tarefas são **salvas automaticamente** — ao recarregar a página, elas permanecem.

---

## 📌 Informações Acadêmicas

| Campo | Informação |
|---|---|
| **Disciplina** | Fundamentos de Web |
| **Discente** | Amanda Mendonça |
| **Curso** | Tecnologia em Ciência dos Dados |
| **Instituição** | UFMS |
| **Ano** | 2025 |
