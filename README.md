## Start

$ export FLASK_APP=banking
$ export FLASK_ENV=development
$ flask run

## Documentação
#### CRUD

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts  |   |  Nova Conta |
| **GET**  | /users/{user_id}/accounts  |   |  Lista Contas |
| **GET**  | /users/{user_id}/accounts/{account_id}  |   |  Detalhes da Conta |
| **PUT**  | /users/{user_id}/accounts/{account_id}  |   |  Atualiza Conta |
| **DELETE**  | /users/{user_id}/accounts/{account_id}  |   |  Deleta Conta |

#### OPERAÇÕES

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **GET**  | /users/{user_id}/accounts/{account_id}/balance   |   |  Consulta Saldo |
| **POST**  | /users/{user_id}/accounts/{account_id}/deposit  |  value (float) | Realiza Depósito  |
| **POST**  | /users/{user_id}/accounts/{account_id}/withdraw   | value (float) |  Realiza Saque |

#### EXTRATO DE TRANSAÇÕES

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts/{account_id}/statement  |  | Lista Transações  |
| **POST**  | /users/{user_id}/accounts/{account_id}/statement  | start_date (YYYY-MM-DD) e end_date (YYYY-MM-DD) | Lista Transações por Período  |

#### BLOQUEIO DA CONTA

|  Método | Endpoint   | Parâmetros | Descrição  |
| ------------ | ------------ | ------------ | ------------ |
| **POST**  | /users/{user_id}/accounts/{account_id}/block  |  | Bloqueia (inativa) Conta  |

