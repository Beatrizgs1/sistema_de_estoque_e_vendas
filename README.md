# Sistema de Estoque e Vendas

**Disciplina:** Estruturas de Dados
**Grupo:** Ana Luisa, Beatriz Gonçalves, Camila Santos, Thiago Lima, Julia Santos

---

## O que e esse projeto

Sistema de linha de comando em Python para controle de produtos, vendas e relatorios.
Permite cadastrar produtos, registrar vendas, buscar por codigo ou nome e gerar
relatorios de estoque baixo e listagens por categoria.

O projeto aplica os conteudos das secoes 2 a 5 da disciplina: Python basico,
complexidade Big-O, vetores nao ordenados e vetores ordenados.

---

## Como executar

Requisito: Python 3.8 ou superior. Nenhuma biblioteca externa necessaria.

```bash
python main.py
```

Ao rodar pela primeira vez o arquivo `dados_estoque.json` sera carregado
automaticamente com os produtos de exemplo.

---

## Funcionalidades

| Opcao | Funcao |
|-------|--------|
| 1 | Cadastrar produto (codigo unico) |
| 2 | Editar produto (nome, preco, quantidade, categoria) |
| 3 | Remover produto pelo codigo |
| 4 | Buscar por codigo — busca binaria O(log n) |
| 5 | Buscar por nome — busca linear O(n) |
| 6 | Registrar venda (valida estoque disponivel) |
| 7 | Listar todos os produtos ordenados por codigo |
| 8 | Listar produtos por categoria |
| 9 | Relatorio de estoque baixo (limite configuravel) |
| 0 | Salvar e sair |

---

## Estrutura de arquivos
sistema_estoque/
├── main.py              # menu interativo e entrada do usuario
├── produto.py           # classe Produto com validacoes
├── estoque.py           # operacoes de cadastro, busca e venda
├── arquivos.py          # salvar e carregar dados em JSON
└── dados_estoque.json   # arquivo de dados com produtos de exemplo

---

## Estruturas de dados — escolhas e justificativa Big-O

### Por que dois vetores?

O sistema mantém dois vetores paralelos que armazenam os mesmos produtos:

**vetor_nao_ordenado** — guarda os produtos na ordem em que foram cadastrados.
Usado exclusivamente para busca por nome, ja que o nome nao e a chave de ordenacao.

**vetor_ordenado** — sempre ordenado por codigo. Usado para busca binaria,
listagem ordenada e relatorios.

Como os dois vetores apontam para os mesmos objetos na memoria, editar um
produto reflete automaticamente nos dois.

---

### Busca por codigo — Busca Binaria O(log n)

Localizado em `estoque.py`.

O vetor esta ordenado por codigo, entao podemos dividir ao meio a cada passo
em vez de olhar elemento por elemento.

Como funciona:
Vetor: [001, 002, 003, 004, 005]
Buscar: 004
Passo 1: meio = 003 → 003 < 004 → busca na metade direita
Passo 2: meio = 004 → encontrado!

Com 1000 produtos a busca linear precisaria de ate 1000 comparacoes.
A busca binaria precisa de no maximo 10 (log2 de 1000 e aproximadamente 10).

**Complexidade: O(log n)**

---

### Busca por nome — Busca Linear O(n)

Tambem em `estoque.py`.

O vetor nao esta ordenado por nome, entao nao e possivel usar busca binaria.
O sistema percorre todos os produtos comparando com o termo buscado.
A busca e parcial e nao diferencia maiusculas de minusculas.

**Complexidade: O(n)**

---

### Insercao no vetor ordenado — O(n)

Ao cadastrar um produto, a posicao correta e encontrada percorrendo o vetor.
Em seguida os elementos sao deslocados para abrir espaco.

**Complexidade: O(n)**

Justificativa: aceitavel para o volume esperado neste sistema.

---

## Regras de negocio

- Codigo de produto nao pode ser duplicado
- Preco deve ser maior que zero
- Quantidade nao pode ser negativa
- Venda nao e registrada se o estoque for insuficiente

---

## Persistencia de dados

Os dados sao salvos automaticamente apos cada operacao de escrita
(cadastro, edicao, remocao e venda) no arquivo `dados_estoque.json`.
Na proxima execucao os dados sao carregados automaticamente.
