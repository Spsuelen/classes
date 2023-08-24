# criando a classe princial que contém um dicionario para guardar as informações que serão inseridas futuramente.

class GerenciadorAcademico: 
    def __init__(self):
        self.__controle = {'dados': []}
        
# Getter no dicionário

    @property 
    def controle (self):
        return self.__controle
    
# Mensagem Padrão    

    def mensagem(self):
        print('Seja bem vindo(a) ao Sitema para Gerenciar a área Acadêmica !!')
    
 # Metodo para inserir informações
    
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
            
# Caso seja necessário esse trecho de código atualizará alguma informação ja inserida anteriormente.

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
# Metodo que lista as informações cadastradas

    def Listar_Informacoes(self):
        if self.__controle['dados']:
            print('Consta no nosso sistema os seguintes dados:')
            for informacao in self.__controle['dados']:
                print(informacao['id'], informacao['nome'], informacao['data_nasc'], informacao['cpf'], informacao['historico'], informacao['media'], informacao['disciplinas_curso'], informacao['horarios_aula'], informacao['frequencia'], informacao['status'])
        else:
          print('Até o momento o sistema segue sem nenhum registro! ')
        
# Metodo para apagar uma informação
            
    def Deletar_Informacao(self,id):
        del self.__controle['dados'][id]
        
# Classe que herdará todas as especificações de GerenciadorAcademico

class Aluno(GerenciadorAcademico):
    def __init__(self,RA):
        super().__init__()
        self.__RA = RA

# Getter no Registro de Aluno
    @property
    def RA(self):
        return self.__RA
    
    def mensagem(self):
        pass
# Método que verifica quais são os as especificações permitidas em Nivel Superior

    def Verificar_Informacoes(self, argumentos):
        permitidos = {'pos','graduacao'}
        if argumentos not in permitidos:
            return "[ATENÇÃO] Nível Acadêmico nao permidido ser inserido."
        return "Nível Superior inserido com sucesso."
    

# Classe que herdará as especificações da classe aluno
   
class NivelSuperior(Aluno):
    def __init__(self, RA,nivel_formacao):
        super().__init__(RA)
        self.__nivel_formacao = nivel_formacao
        
# Getter em Nivel de Formação

    @property
    def nivel_formacao(self):
        return self.__nivel_formacao
    
# Classe que herdará as especificações da classe GerenciadorAcademico
       
class Professor(GerenciadorAcademico):
    def __init__(self,matricula,salario,percentual):
        super().__init__()
        self.__matricula = matricula
        self.salario = salario
        self.percentual = percentual
        
#Getter em matricula
        
    @property
    def matricula(self):
        return self.__matricula
    
# Setter em matricula para permitir que ele aceite somente valores e seu tamanho unico de 5 caracteres
    
    @matricula.setter
    def matricula(self,num):
        if num.isnumeric() and len(num) == 5:
            self.__matricula = num
            print('A Senha fornecida está correta. ')  
        else:
            print('Verifique a senha e tente novamente.')
            
     
        
# Metodo que verifica o reajuste salarial
    
    def Reajuste_Salarial(self):
        self.__salario = self.__salario +(self.__salario * (self.__percentual / 100))
        print(f' Seu salario com um aumento de {self.__percentual} % esta no valor de R$ {self.__salario}')
        
#Getter percetual de reajuste    

    @property
    def percentual(self):
        return self.__percentual

# Setter para configurar o valor que for inserido em percentual
 
    @percentual.setter
    def percentual(self,tipo):
        if isinstance(tipo, str):
            tipo = float(tipo.replace('%', ''))
            
        self.__percentual = tipo
            
# Getter em salário

    @property
    def salario(self):
        return self.__salario
    
# Setter para configurar o valor que for inserido em salario
    
    @salario.setter
    def salario(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self.__salario = valor
        
# Classe que herdará as especificações da classe professor
    
class Ocupacao(Professor):
     def __init__(self,matricula,salario,percentual,ocupacao):
         super().__init__(matricula,salario,percentual)
         self.__ocupacao = ocupacao

# Getter em ocupacao

     @property
     def ocupacao(self):
         return self.__ocupacao

#  Método que verifica quais são os as especificações permitidas em ocupação.
# Incluso um casting para como ele escrever o valor permitido, o programa transforme em minusculo para a validação.
     
     def Verificar_Ocupacao(self, nome):
         valor = {'efetivo','temporario'}
         nome = nome.lower()
         if nome not in valor:
             print("[ATENÇÃO] Ocupação nao permidida ser inserida.") 
         else:
             print("Ocupacao inserida com sucesso.")
    

controle = GerenciadorAcademico()


   

professor = Professor('',1500.00,10)
professor.matricula = '1'










