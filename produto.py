class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        if not codigo or not codigo.strip():
            raise ValueError("Codigo nao pode ser vazio.")
        if not nome or not nome.strip():
            raise ValueError("Nome nao pode ser vazio.")
        if not categoria or not categoria.strip():
            raise ValueError("Categoria nao pode ser vazia.")
        if preco <= 0:
            raise ValueError("Preco deve ser maior que zero.")
        if quantidade < 0:
            raise ValueError("Quantidade nao pode ser negativa.")

        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "quantidade": self.quantidade,
        }
