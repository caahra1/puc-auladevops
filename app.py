# app.py

def somar(a, b):
    """Soma dois números."""
    return a + b

def subtrair(a, b):
    """Subtrai o segundo número do primeiro."""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números."""
    return a * b

def dividir(a, b):
    """Divide o primeiro número pelo segundo."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def saudar(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"