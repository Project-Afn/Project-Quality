# API de Gerenciamento de Itens

Esta é uma API RESTful construída com FastAPI para gerenciamento de itens.

## Funcionalidades

- Listar todos os itens
- Obter um item específico por ID
- Criar novos itens
- Verificação de saúde da API

## Requisitos

- Python 3.7+
- FastAPI
- Pydantic

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install fastapi uvicorn
```

## Executando a API

Para iniciar o servidor, execute:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Endpoints

### GET /
- Retorna uma mensagem de boas-vindas

### GET /health
- Verifica o status da API
- Retorna informações sobre a versão e serviços

### GET /items
- Lista todos os itens cadastrados
- Retorna uma lista de itens

### GET /items/{item_id}
- Obtém um item específico pelo ID
- Retorna os detalhes do item ou erro 404 se não encontrado

### POST /items
- Cria um novo item
- Corpo da requisição:
```json
{
    "nome": "string",
    "descricao": "string (opcional)"
}
```

## Modelo de Dados

```python
class Item:
    id: Optional[int]
    nome: str
    descricao: Optional[str]
``` 