# API Python com FastAPI

Esta é uma API simples construída com FastAPI que permite gerenciar itens.

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
uvicorn main:app --reload
```

## Testes

Para executar os testes automatizados:
```bash
pytest test_main.py -v
```

### CI/CD
Os testes são executados automaticamente através do GitHub Actions quando:
- Um push é feito para a branch `main`
- Um Pull Request é criado para a branch `main`

O workflow testa a aplicação em diferentes versões do Python (3.9, 3.10 e 3.11).

## Endpoints

### GET /
- Retorna uma mensagem de boas-vindas

### GET /items
- Lista todos os itens cadastrados

### GET /items/{item_id}
- Retorna um item específico pelo ID

### POST /items
- Cria um novo item
- Exemplo de corpo da requisição:
```json
{
    "nome": "Exemplo",
    "descricao": "Descrição do exemplo"
}
```

## Documentação
A documentação interativa da API está disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 