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

# aula hoje

class Validador(object):
    def __init__(self):
        self._cod_area = (11, 12, 19, 65, 68, 92, 93)
        
    def ano_bissexto(self, ano):
        pass
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False

    def validar_data(self, data):
        pass
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        meses_de_31 = (1, 3, 5, 7, 8, 10, 12)
        meses_de_30 = (4, 6, 9, 11)

        ano_valido = False
        if ano > 0 and len(data[6:])==4:
            ano_valido = True

        mes_valido = False
        if mes > 0 and mes < 13:
           mes_valido = True

        dia_valido = False
        if dia > 0 and dia < 32:
            if dia == 31:
                if mes in meses_de_31:
                    dia_valido = True
            elif dia == 30:
                if mes in meses_de_30 or mes in meses_de_31:
                    dia_valido = True
            elif dia == 29:
                if mes != 2:
                    dia_valido = True
                elif mes == 2 and self.ano_bissexto(ano):
                    dia_valido = True
            else:
                dia_valido = True

        data_valida = False
        if ano_valido and mes_valido and dia_valido:
            data_valida = True

        return data_valida

    # (92)999679090
    def validar_telefone(self, telefone):
        
        telefone_valido = True
        if len(telefone) != 13:
            telefone_valido = False
        elif len(telefone[4:]) != 9:
            telefone_valido = False
        elif telefone[0] != '(' or telefone[3] != ')':
            telefone_valido = False
        elif int(telefone[1:3]) not in self._cod_area:
            telefone_valido = False
        print (telefone_valido)
        return telefone_valido

##teste
import validador as val

class TestTelefone(object):
#    def test_ddd_invalido(self):
#       v = val.Validador()
#        telefone = '(9)999664444'
#        assert v.validar_telefone(telefone) == False
    
    def teste_tam_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('92999984567') == False
    
    def test_cod_area_invalido (self):
        v = val.Validador()
        assert v.validar_telefone ('(00)999984567') == False
    
    def test_format_cod_area_invalido(self):
        v = v.Validador()
        assert v.validar_telefone ('[92]99998456') == False

class TestData(object):
    def test_data_dia_invalido(self):
        v = val.Validador()
        assert v.validar_data("00/09/2022") == False
        assert v.validar_data("32/09/2022") == False

pip install pytest
pip install coverage
pytest --version
coverage --version
pytest nome.py
