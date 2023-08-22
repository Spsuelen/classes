import validador as val

class TestTelefone(object):
    def test_ddd_invalido(self):
        v = val.validador()
        telefone = '(9)999664444'
        assert v.validar_telefone(telefone) == False
    
    def teste_tam_invalido(self):
        v = val.validador()
        assert v.validar_telefone('92999984567') == False
    
    def test_cod_area_invalido (self):
        v = val.validador()
        assert v.validar_telefone ('(00)999984567') == False
    
    def test_format_cod_area_invalido(self):
        v = val.validador()
        assert v.validar_telefone ('[92]99998456') == False

class TestData(object):
    def test_data_dia_invalido(self):
        v = val.validador()
        assert v.validar_data("00/09/2022") == False
        assert v.validar_data("32/09/2022") == False