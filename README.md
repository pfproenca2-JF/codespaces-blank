# Desafio: API Bancária Assíncrona com FastAPI

Este repositório contém uma implementação mínima da API bancária solicitada no desafio.

Como executar (local):

1. Criar e ativar um ambiente virtual (recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Rodar a aplicação

```bash
uvicorn main:app --reload
```

3. Endpoints principais

- `POST /auth/login` — criar token JWT (enviar `{ "user_id": <int> }`).
- `GET /accounts/` — listar contas (requer Authorization: Bearer <token>).
- `POST /accounts/` — criar conta.
- `POST /transactions/` — criar transação (depósito/saque).

Observações:
- Para simplificar o desafio, o endpoint de login aceita qualquer `user_id` e retorna um JWT.
- A base de dados padrão é `sqlite:///./test.db` definida em `config.py`.
