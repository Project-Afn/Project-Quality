from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Minha API")

# Modelo de dados para os itens
class Item(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: Optional[str] = None

# Lista para armazenar os itens (simulando um banco de dados)
items = []
contador_id = 1

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API!"}

@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "versao": "1.0.0",
        "servicos": {
            "api": "operacional",
            "banco_dados": "operacional"
        }
    }

@app.get("/items", response_model=List[Item])
async def listar_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def obter_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/items", response_model=Item)
async def criar_item(item: Item):
    global contador_id
    item.id = contador_id
    contador_id += 1
    items.append(item)
    return item 