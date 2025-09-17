# test/test_app.py

import pytest
# Importamos as funções do arquivo app.py que está na raiz
from app import somar, subtrair, multiplicar, dividir, saudar

# Teste 1: Soma
def test_somar():
    assert somar(5, 5) == 10

# Teste 2: Subtração
def test_subtrair():
    assert subtrair(10, 4) == 6

# Teste 3: Multiplicação
def test_multiplicar_por_zero():
    assert multiplicar(10, 0) == 0

# Teste 4: Divisão com erro esperado
def test_dividir_por_zero_deve_lancar_erro():
    with pytest.raises(ValueError):
        dividir(5, 0)

# Teste 5: Saudação
def test_saudar():
    assert saudar("Mundo") == "Olá, Mundo!"