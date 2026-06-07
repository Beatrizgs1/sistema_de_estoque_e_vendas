import json
import os

from produto import Produto

ARQUIVO = "dados_estoque.json"


def salvar(produtos, caminho=ARQUIVO):
    dados = []
    for p in produtos:
        dados.append(p.to_dict())

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"  Dados salvos em '{caminho}'.")


def carregar(caminho=ARQUIVO):
    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    produtos = []
    for d in dados:
        p = Produto(
            codigo=d["codigo"],
            nome=d["nome"],
            categoria=d["categoria"],
            preco=float(d["preco"]),
            quantidade=int(d["quantidade"]),
        )
        produtos.append(p)

    return produtos