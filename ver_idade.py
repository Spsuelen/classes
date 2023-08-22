from idade import verificar_idade

def teste_verificar_idade():
    assert verificar_idade(19) == 19
    assert verificar_idade(12) is None
    assert verificar_idade(15) is None
    assert verificar_idade(10) is None
    assert verificar_idade(50) == 50
    assert verificar_idade(51) == 51
    assert verificar_idade(45) == 45
    assert verificar_idade(78) == 78
    assert verificar_idade(81) == 81
    assert verificar_idade(65) == 65
     