from fastapi.testclient import TestClient
from main import app, items

client = TestClient(app)

def setup_function():
    # Limpa a lista de itens antes de cada teste
    items.clear()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo à API!"}

def test_criar_item():
    item_data = {
        "nome": "Item Teste",
        "descricao": "Descrição do item teste"
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == item_data["nome"]
    assert data["descricao"] == item_data["descricao"]
    assert data["id"] is not None

def test_listar_items():
    # Primeiro, criamos um item
    item_data = {
        "nome": "Item para Lista",
        "descricao": "Item para testar listagem"
    }
    client.post("/items", json=item_data)
    
    # Agora testamos a listagem
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_obter_item_especifico():
    # Primeiro, criamos um item
    item_data = {
        "nome": "Item Específico",
        "descricao": "Item para testar busca específica"
    }
    response = client.post("/items", json=item_data)
    item_id = response.json()["id"]
    
    # Agora testamos a busca do item específico
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["nome"] == item_data["nome"]

def test_obter_item_inexistente():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item não encontrado" 