import pytest
from app import app as flask_app  # Importa a sua aplicação Flask do arquivo app.py

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

# --- Aqui começam os 5 testes unitários ---

# Teste 1: Verifica se a página principal (/) responde com sucesso (código 200)
def test_hello_world_status_code(client):
    """Verifica se a rota principal retorna o status code 200 OK."""
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica se o conteúdo da página principal está correto
def test_hello_world_content(client):
    """Verifica se a mensagem 'Meu container Docker esta funcionando!' está na página."""
    response = client.get('/')
    assert b"Meu container Docker esta funcionando!" in response.data

# Teste 3: Verifica se o tipo de conteúdo da resposta é HTML
def test_hello_world_content_type(client):
    """Verifica se o cabeçalho Content-Type é text/html."""
    response = client.get('/')
    assert 'text/html' in response.content_type

# Teste 4: Um teste simples que sempre passa, para garantir
def test_always_passes():
    """Este é um teste de exemplo que sempre será bem-sucedido."""
    assert True

# Teste 5: Verifica se uma rota inexistente retorna 'Não Encontrado' (código 404)
def test_not_found_route(client):
    """Verifica se ao acessar uma rota que não existe, o status code é 404."""
    response = client.get('/pagina-que-nao-existe')
    assert response.status_code == 404
