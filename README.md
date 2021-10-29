## Dock Tech API Flask

### Pré-resquisitos
- Python 3.8
- Docker

### Run

#### localhost

```shell
# clone
$ git clone https://github.com/jhonataneduardo/dock-api-banking-flask.git
$ cd dock-api-banking-flask
$ python3 -m venv venv

# virtualenv
$ source venv/bin/activate

# requirements
$ pip install -r requirements.txt

# env
$ export FLASK_APP=banking
$ export FLASK_ENV=development

# tests
$ pytest

# dataload
$ flask dataload createuser DockTech

# run
$ flask run
```
#### Docker
$ docker-compose up
Acesse: http://localhost:5000

### Dados de demostração
**USER (Pessoa)**

```json
{
    "id": 1,
    "name": "DockTech",
    "cpf": "12345678912",
    "birth_date": "1991-07-13"
  }
```

**ACCOUNT (Conta)**

```json
{
    "id": 1,
    "user_id": 1,
    "balance": 1080.0,
    "withdrawal_limit_day": 100.0,
    "active": true,
    "type": 1234,
    "date_created": "2021-10-29"
  }
```

### Documentação

#### CRUD

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts  |   |  Nova Conta |
| **GET**  | /users/{user_id}/accounts  |   |  Lista Contas |
| **GET**  | /users/{user_id}/accounts/{account_id}  |   |  Detalhes da Conta |
| **PUT**  | /users/{user_id}/accounts/{account_id}  |   |  Atualiza Conta |
| **DELETE**  | /users/{user_id}/accounts/{account_id}  |   |  Deleta Conta |

#### Operaçoes

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **GET**  | /users/{user_id}/accounts/{account_id}/balance   |   |  Consulta Saldo |
| **POST**  | /users/{user_id}/accounts/{account_id}/deposit  |  value (float) | Realiza Depósito  |
| **POST**  | /users/{user_id}/accounts/{account_id}/withdraw   | value (float) |  Realiza Saque |

#### Extrato de Transações

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts/{account_id}/statement  |  | Lista Transações  |
| **POST**  | /users/{user_id}/accounts/{account_id}/statement  | start_date (YYYY-MM-DD) e end_date (YYYY-MM-DD) | Lista Transações por Período  |

#### Bloqueio da Conta

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts/{account_id}/block  |  | Bloqueia (inativa) Conta  |

