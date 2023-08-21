class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def inserir(self,produto):
        self.produtos.append(produto)
        
    def lista(self):
        for produto in self.produtos:
            print(produto.nome,produto.valor)   
    def soma(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total            
        
        
class Produto:
    def __init__(self,nome,valor):
        self.__nome = nome
        self.__valor = valor
    @property
    def nome(self):
        return self.__nome
    @property
    def valor(self):
        return self.__valor

carrinho = Carrinho()
p1 = Produto('Camiseta',50)
p2 = Produto('Moletom',170)
p3 = Produto('saia',255)
carrinho.inserir(p1)
carrinho.inserir(p2)
carrinho.inserir(p3)
carrinho.lista()
print(carrinho.soma())