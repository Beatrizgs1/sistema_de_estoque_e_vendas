# Sistema de Estoque e Vendas

Sistema de linha de comando em Python para controle de produtos, vendas e relatorios.

## Como executar

```bash
python main.py
```

Nao precisa instalar nenhuma biblioteca extra. Apenas Python 3.8 ou superior.

## Funcionalidades

| Opcao | Funcao |
|-------|--------|
| 1 | Cadastrar produto |
| 2 | Editar produto |
| 3 | Remover produto |
| 4 | Buscar por codigo — busca binaria O(log n) |
| 5 | Buscar por nome — busca linear O(n) |
| 6 | Registrar venda |
| 7 | Listar todos ordenados por codigo |
| 8 | Listar por categoria |
| 9 | Relatorio de estoque baixo |
| 0 | Salvar e sair |

## Estrutura de arquivos

- main.py — menu e fluxo principal
- produto.py — classe Produto e validacoes
- estoque.py — operacoes de cadastro, busca e venda
- arquivos.py — salvar e carregar dados em JSON
- dados_estoque.json — arquivo de dados

## Escolhas tecnicas

### Por que dois vetores?

O sistema usa dois vetores para cada produto:
- vetor_nao_ordenado: guarda os produtos na ordem de insercao. Usado para busca por nome.
- vetor_ordenado: sempre ordenado por codigo. Usado para busca binaria e listagem.

### Busca por codigo — Busca Binaria O(log n)

O vetor esta ordenado por codigo, entao podemos dividir ao meio a cada passo.
Com 1000 produtos, sao no maximo 10 comparacoes (log2 de 1000 ≈ 10).

Exemplo:
  Vetor: [001, 002, 003, 004, 005]
  Buscar: 004
  Passo 1: meio = 003 < 004 → busca a direita
  Passo 2: meio = 004 == 004 → ENCONTRADO

### Busca por nome — Busca Linear O(n)

O vetor nao esta ordenado por nome, entao precisamos olhar um por um.
Com 1000 produtos, sao ate 1000 comparacoes no pior caso.

