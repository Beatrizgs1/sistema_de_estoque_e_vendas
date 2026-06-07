from produto import Produto

class Estoque:
    def __init__(self):
        self.vetor_nao_ordenado = []  
        self.vetor_ordenado = []      

    def buscar_por_codigo(self, codigo):
        esquerda = 0
        direita = len(self.vetor_ordenado) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            codigo_meio = self.vetor_ordenado[meio].codigo

            if codigo_meio == codigo:
                return self.vetor_ordenado[meio]
            elif codigo_meio < codigo:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return None  
    
    def _inserir_ordenado(self, produto):
        posicao = 0
        for i in range(len(self.vetor_ordenado)):
            if self.vetor_ordenado[i].codigo < produto.codigo:
                posicao = i + 1
            else:
                break
        self.vetor_ordenado.insert(posicao, produto)

    def cadastrar(self, produto):
        if self.buscar_por_codigo(produto.codigo) is not None:
            raise ValueError(f"Ja existe um produto com o codigo '{produto.codigo}'.")

        self.vetor_nao_ordenado.append(produto)
        self._inserir_ordenado(produto)

    def editar(self, codigo, nome=None, preco=None, quantidade=None, categoria=None):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise KeyError(f"Produto '{codigo}' nao encontrado.")

        if nome is not None:
            if not nome.strip():
                raise ValueError("Nome nao pode ser vazio.")
            produto.nome = nome

        if preco is not None:
            if preco <= 0:
                raise ValueError("Preco deve ser maior que zero.")
            produto.preco = preco

        if quantidade is not None:
            if quantidade < 0:
                raise ValueError("Quantidade nao pode ser negativa.")
            produto.quantidade = quantidade

        if categoria is not None:
            if not categoria.strip():
                raise ValueError("Categoria nao pode ser vazia.")
            produto.categoria = categoria

        return produto

    def remover(self, codigo):
        """Remove um produto pelo codigo."""
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise KeyError(f"Produto '{codigo}' nao encontrado.")

        self.vetor_nao_ordenado.remove(produto)
        self.vetor_ordenado.remove(produto)
        return produto

    def buscar_por_nome(self, termo):
        termo = termo.lower()
        resultado = []
        for produto in self.vetor_nao_ordenado:
            if termo in produto.nome.lower():
                resultado.append(produto)
        return resultado

    def registrar_venda(self, codigo, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade vendida deve ser maior que zero.")

        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise KeyError(f"Produto '{codigo}' nao encontrado.")

        if produto.quantidade < quantidade:
            raise ValueError(
                f"Estoque insuficiente. Disponivel: {produto.quantidade}, "
                f"solicitado: {quantidade}."
            )

        produto.quantidade -= quantidade
        return produto

    def listar_ordenado(self):
        return list(self.vetor_ordenado)

    def listar_por_categoria(self, categoria):
        resultado = []
        for produto in self.vetor_ordenado:
            if produto.categoria.lower() == categoria.lower():
                resultado.append(produto)
        return resultado

    def relatorio_estoque_baixo(self, limite):
        resultado = []
        for produto in self.vetor_ordenado:
            if produto.quantidade < limite:
                resultado.append(produto)
        return resultado

    def carregar_lista(self, produtos):
        self.vetor_nao_ordenado = []
        self.vetor_ordenado = []
        for produto in produtos:
            self.cadastrar(produto)

    def total(self):
        return len(self.vetor_ordenado)
