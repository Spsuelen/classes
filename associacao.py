class Escritor:
    def __init__(self,nome):
        self.__nome = nome #atributo privado
        self.__ferramenta = None
    def mensagem(self):
        print(f'Seja bem vindo {self.__nome}')
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta
    
class Caneta:
    def __init__(self,cor):
        self.__cor = cor
        #print(f'Minha linda cor é {self.__cor}')

    @property
    def cor(self):
        return self.__cor
    def msg(self):
        print('Silêncio !! Estou trabalhando')

class Papel:
    def __init__(self,tipo):
        self.__tipo = tipo
        #print(f'Sou do tipo {self.__tipo}')
    @property
    def papel(self):
        return self.__tipo
    def msg(self):
        print('Atenção estou escolhendo as palavras certas para escrever')
    
escritor = Escritor ('Gabriel')
#escritor.mensagem()
caneta = Caneta('Azul')
#caneta.msg()
papel = Papel('A4')
escritor.ferramenta = papel
escritor.ferramenta.msg()
