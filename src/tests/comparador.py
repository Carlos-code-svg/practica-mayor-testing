from src.comparador import mayor

def test_numeros_distintos():
    assert mayor(10, 5) == 10
    assert mayor(3, 8) == 8

def test_numeros_iguales():
    assert mayor(7, 7) == 7

def test_numeros_negativos():
    assert mayor(-3, -10) == -3
    assert mayor(-5, 2) == 2
