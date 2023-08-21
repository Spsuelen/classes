class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf 
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf
    def apresentacao(self):
        print(f'Me chamo {self.__nome}, tenho {self.__idade} e possuo o cpf {self.__cpf}')
class Filho(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
    def mensagem(self):
        print('Estou na classe Filho, ou seja sou uma herança')
    

filho = Filho('Ana',41,'015.862.952-33')
filho.apresentacao()