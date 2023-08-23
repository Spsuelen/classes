## CRIANDO UMA CLASSE PARA GERENCIAMENTO ACADEMICO CRIANDO UM DICIONARIO PRIVADO PARA RECEBER AS INFORMAÇOES
class GerenciadorAcademico: 
    def __init__(self):
        self.__controle = {'dados': []}
        
##GETTER DO DICIONARIO
    @property 
    def controle (self):
        return self.__controle
    
 ## CRIANDO UM METODO PARA INSERIR INFORMAÇÃO 
    
    def Inserir_Informacao_Gerenciador(self,id,nome,data_nasc,cpf,historico,media,disciplinas_curso,horarios_aula,frequencia,status):
        
        if 'dados' not in self.__controle:
            valores = {"id": id,
            "nome": nome,
            "data_nasc": data_nasc,
            "cpf": cpf,
            "historico": historico,
            "media": media,
            "disciplinas_curso": disciplinas_curso,
            "horarios_aula": horarios_aula,
            "frequencia": frequencia,
            "status": status
        }
            self.__controle['dados'].append(valores)
 ## COMANDO PARA ATUALIZAR AS INFORMAÇOES JÁ INSERIDA
        else: 
         self.__controle['dados'].append(
             {"id": id,
            "nome": nome,
            "data_nasc": data_nasc,
            "cpf": cpf,
            "historico": historico,
            "media": media,
            "disciplinas_curso": disciplinas_curso,
            "horarios_aula": horarios_aula,
            "frequencia": frequencia,
            "status": status
        }
         )
##VERIFICANDO INFORMAÇÕES CADASTRADAS NO SISTEMA
    def Listar_Informacoes(self):
        if self.__controle['dados']:
            print('Consta no nosso sistema os seguintes dados:')
            for informacao in self.__controle['dados']:
                print(informacao['id'], informacao['nome'], informacao['data_nasc'], informacao['cpf'], informacao['historico'], informacao['media'], informacao['disciplinas_curso'], informacao['horarios_aula'], informacao['frequencia'], informacao['status'])
        else:
          print('Até o momento o sistema segue sem nenhum registro! ')
        
## APAGANDO ALGUMA INFORMAÇÃO
            
    def apaga_(self,id):
        del self.__controle['dados'][id]
        
##CRIANDO A CLASSE ALUNO HERDANDO AS ESPECIFICAÇÕES DE GERENCIADOR ACADEMICO

class Aluno(GerenciadorAcademico):
    def __init__(self,RA):
        super().__init__()
        self.__RA = RA
    @property
    def RA(self):
        return self.__RA
    def mensagem(self):
        pass

##CRIANDO A CLASSE NIVEL SUPERIOR HERDANDO AS ESPECIFICAÇÕES DE ALUNO   
class NivelSuperior(Aluno):
    def __init__(self, RA,nivel_formacao):
        super().__init__(RA)
        self.__nivel_formacao = nivel_formacao
    @property
    def nivel_formacao(self):
        return self.__nivel_formacao
    def mensagem(self):
        pass


        
# controle = GerenciadorAcademico()
# controle.Inserir_Informacao_Gerenciador(1,'Maria Julia','2000-02-09','000.000.000-00','xx','xx','Python - Nivelamento','18:00:00','xx','Ativo(a)')
# controle.Inserir_Informacao_Gerenciador(2,'Victor Gabriel','1980-08-01','111.111.111-11','xx','xx','Python - Nivelamento','18:00:00','xx','Ativo(a)')
# controle.Inserir_Informacao_Gerenciador(3,'Pedro Henerique','1999-01-01','222.222.222-22','xx','xx','Python - Nivelamento','18:00:00','xx','Ativo(a)')
# controle.Listar_Informacoes()



# Criando uma instância da classe Aluno e inserindo informações
aluno = Aluno('123')
aluno.Inserir_Informacao_Gerenciador(4, 'SARAH FERNANDA', '2001-10-12', '333.333.333-33', 'xx', 'xx', 'Python - Nivelamento', '18:00:00', 'xx', 'Ativo(a)')

# Criando uma instância da classe NivelSuperior e inserindo informações
aluno_nivel_superior = NivelSuperior('456','Graduação')
aluno_nivel_superior.Inserir_Informacao_Gerenciador(5, 'AMANDA CARLA', '1992-03-25', '444.444.444-44', 'xx', 'xx', 'Python - Nivelamento', '18:00:00', 'xx', 'Ativo(a)')

# Listando informações do aluno e aluno de nível superior
aluno.Listar_Informacoes()
print(f'Minha matricula ativa é {aluno.RA}')

aluno_nivel_superior.Listar_Informacoes()
print(f'Minha matricula é {aluno_nivel_superior.RA}')
print(f'Meu nivel superior atualmente é {aluno_nivel_superior.nivel_formacao}')