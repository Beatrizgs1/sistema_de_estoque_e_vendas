import os
import arquivos
from estoque import Estoque
from produto import Produto

LIMITE_BAIXO = 5


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")


def linha():
    print("-" * 50)


def ler_texto(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("  Este campo nao pode ser vazio.")


def ler_float(prompt):
    while True:
        try:
            valor = float(input(prompt).strip().replace(",", "."))
            if valor <= 0:
                print("  O valor deve ser positivo.")
                continue
            return valor
        except ValueError:
            print("  Digite um numero valido. Ex: 19.90")


def ler_inteiro(prompt, minimo=0):
    while True:
        try:
            valor = int(input(prompt).strip())
            if valor < minimo:
                print(f"  O valor deve ser pelo menos {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Digite um numero inteiro valido.")


def exibir_produto(p):
    print(f"  [{p.codigo}] {p.nome}")
    print(f"      Categoria : {p.categoria}")
    print(f"      Preco     : R$ {p.preco:.2f}")
    print(f"      Quantidade: {p.quantidade} unid.")
    print()


def exibir_lista(produtos, titulo):
    linha()
    print(f"  {titulo}")
    linha()
    if not produtos:
        print("  Nenhum produto encontrado.")
        return
    for p in produtos:
        exibir_produto(p)
    print(f"  Total: {len(produtos)} produto(s).")

def cadastrar(estoque):
    linha()
    print("  CADASTRAR PRODUTO")
    linha()
    codigo = ler_texto("  Codigo   : ")
    nome = ler_texto("  Nome     : ")
    categoria = ler_texto("  Categoria: ")
    preco = ler_float("  Preco R$ : ")
    quantidade = ler_inteiro("  Qtd.     : ", minimo=0)

    try:
        produto = Produto(codigo, nome, categoria, preco, quantidade)
        estoque.cadastrar(produto)
        print(f"\n  Produto '{nome}' cadastrado com sucesso!")
    except ValueError as e:
        print(f"\n  Erro: {e}")


def editar(estoque):
    linha()
    print("  EDITAR PRODUTO")
    linha()
    codigo = ler_texto("  Codigo do produto: ")

    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print(f"\n  Produto '{codigo}' nao encontrado.")
        return

    exibir_produto(produto)
    print("  Deixe em branco para manter o valor atual.\n")

    nome = input(f"  Novo nome [{produto.nome}]: ").strip() or None
    categoria = input(f"  Nova categoria [{produto.categoria}]: ").strip() or None

    preco = None
    entrada = input(f"  Novo preco [{produto.preco:.2f}]: ").strip()
    if entrada:
        try:
            preco = float(entrada.replace(",", "."))
        except ValueError:
            print("  Preco invalido, mantendo valor atual.")

    quantidade = None
    entrada = input(f"  Nova quantidade [{produto.quantidade}]: ").strip()
    if entrada:
        try:
            quantidade = int(entrada)
        except ValueError:
            print("  Quantidade invalida, mantendo valor atual.")

    try:
        estoque.editar(codigo, nome=nome, preco=preco, quantidade=quantidade, categoria=categoria)
        print("\n  Produto atualizado com sucesso!")
    except (KeyError, ValueError) as e:
        print(f"\n  Erro: {e}")


def remover(estoque):
    linha()
    print("  REMOVER PRODUTO")
    linha()
    codigo = ler_texto("  Codigo do produto: ")

    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print(f"\n  Produto '{codigo}' nao encontrado.")
        return

    exibir_produto(produto)
    confirmacao = input("  Confirmar remocao? [S/N]: ").strip().upper()
    if confirmacao == "S":
        estoque.remover(codigo)
        print("\n  Produto removido com sucesso!")
    else:
        print("\n  Operacao cancelada.")


def buscar_codigo(estoque):
    linha()
    print("  BUSCAR POR CODIGO  (Busca Binaria - O(log n))")
    linha()
    codigo = ler_texto("  Codigo: ")
    produto = estoque.buscar_por_codigo(codigo)
    if produto:
        exibir_produto(produto)
    else:
        print(f"\n  Produto '{codigo}' nao encontrado.")


def buscar_nome(estoque):
    linha()
    print("  BUSCAR POR NOME  (Busca Linear - O(n))")
    linha()
    termo = ler_texto("  Nome (parcial): ")
    resultados = estoque.buscar_por_nome(termo)
    exibir_lista(resultados, f"Resultados para '{termo}'")


def registrar_venda(estoque):
    linha()
    print("  REGISTRAR VENDA")
    linha()
    codigo = ler_texto("  Codigo do produto: ")
    quantidade = ler_inteiro("  Quantidade vendida: ", minimo=1)

    try:
        produto = estoque.registrar_venda(codigo, quantidade)
        print(f"\n  Venda registrada! Estoque restante de '{produto.nome}': {produto.quantidade} unid.")
    except (KeyError, ValueError) as e:
        print(f"\n  Erro: {e}")


def listar_ordenado(estoque):
    produtos = estoque.listar_ordenado()
    exibir_lista(produtos, "PRODUTOS ORDENADOS POR CODIGO")


def listar_categoria(estoque):
    linha()
    print("  LISTAR POR CATEGORIA")
    linha()
    categoria = ler_texto("  Categoria: ")
    produtos = estoque.listar_por_categoria(categoria)
    exibir_lista(produtos, f"Categoria: {categoria}")


def estoque_baixo(estoque):
    global LIMITE_BAIXO
    linha()
    print("  RELATORIO DE ESTOQUE BAIXO")
    linha()
    entrada = input(f"  Limite atual: {LIMITE_BAIXO}. Novo limite (Enter para manter): ").strip()
    if entrada:
        try:
            LIMITE_BAIXO = int(entrada)
        except ValueError:
            print("  Limite invalido, mantendo valor atual.")

    produtos = estoque.relatorio_estoque_baixo(LIMITE_BAIXO)
    exibir_lista(produtos, f"Produtos com estoque abaixo de {LIMITE_BAIXO}")

def menu():
    print("\n" + "=" * 50)
    print("  SISTEMA DE ESTOQUE E VENDAS")
    print("=" * 50)
    print("  [1] Cadastrar produto")
    print("  [2] Editar produto")
    print("  [3] Remover produto")
    print("  [4] Buscar por codigo (binaria)")
    print("  [5] Buscar por nome   (linear)")
    print("  [6] Registrar venda")
    print("  [7] Listar todos")
    print("  [8] Listar por categoria")
    print("  [9] Relatorio estoque baixo")
    print("  [0] Sair")
    print("=" * 50)


def main():
    estoque = Estoque()

    try:
        produtos_salvos = arquivos.carregar()
        estoque.carregar_lista(produtos_salvos)
        print(f"  {estoque.total()} produto(s) carregado(s).")
    except Exception as e:
        print(f"  Erro ao carregar dados: {e}")

    while True:
        limpar_tela()
        menu()
        print(f"  Produtos cadastrados: {estoque.total()}")

        opcao = input("\n  Escolha: ").strip()

        limpar_tela()

        if opcao == "1":
            cadastrar(estoque)
        elif opcao == "2":
            editar(estoque)
        elif opcao == "3":
            remover(estoque)
        elif opcao == "4":
            buscar_codigo(estoque)
        elif opcao == "5":
            buscar_nome(estoque)
        elif opcao == "6":
            registrar_venda(estoque)
        elif opcao == "7":
            listar_ordenado(estoque)
        elif opcao == "8":
            listar_categoria(estoque)
        elif opcao == "9":
            estoque_baixo(estoque)
        elif opcao == "0":
            print("\n  Salvando dados...")
            arquivos.salvar(estoque.listar_ordenado())
            print("  Ate logo!")
            break
        else:
            print("  Opcao invalida. Escolha entre 0 e 9.")

        if opcao in {"1", "2", "3", "6"}:
            arquivos.salvar(estoque.listar_ordenado())

        pausar()

if __name__ == "__main__":
    main()
