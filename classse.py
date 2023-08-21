class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mensagem(self):
        print(f'Você está comprando o produto {self.nome} de valor {self.preco}')
    def desconto(self,val):
        self.preco = self.preco - (self.preco * (val / 100))
        print(f'Seu produto terá o preco final de R$ {self.preco} reais')
        
p1 = Produto('Cadeira',1500)
p1.mensagem()
p1.desconto(10) 
