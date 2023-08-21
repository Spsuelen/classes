class Filme:
    def __init__(self):
        self.__lista = {}
        
    @property
    def lista (self):
        return self.__lista
    
    def InserirFilme(self,id,nome):
        if 'dados' not in self.__lista:
            self.__lista['dados'] = {id: nome}
        else:
            self.__lista['dados'].update({id: nome})
    def lista_filme(self):
        for id, nome in self.__lista['dados'].items():
            print(id,nome)
            
    def apaga_filme(self,id):
        del self.__lista['dados'][id]

base = Filme()
base.InserirFilme(1,'Mulher Maravilha')
base.InserirFilme(2,'Homem Aranha')
base.InserirFilme(3,'Besouro Azul')
print(base.lista)
#base.lista_filme()
#base.__lista = 'meu nome é suelen'
#print(base.__lista)
#print(base._Filme__lista)


        
        