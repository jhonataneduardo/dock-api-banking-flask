from app.api.account import AccountListCreate, AccountRetrieveUpdateDestroy
from app.api.user import UserListCreate, UserRetrieveUpdateDestroy
from app.api.transaction import TransactionListCreate, TransactionRetrieveUpdateDestroy


def routes_app(api):
    api.add_resource(
        UserListCreate,
        '/users'
    )
    api.add_resource(
        UserRetrieveUpdateDestroy,
        '/users/<int:user_id>'
    )
    api.add_resource(
        AccountListCreate,
        '/users/<int:user_id>/accounts'
    )
    api.add_resource(
        AccountRetrieveUpdateDestroy,
        '/users/<int:user_id>/accounts/<int:account_id>'
    )
    api.add_resource(
        TransactionListCreate,
        '/users/<int:user_id>/accounts/<int:account_id>/transactions'
    )
    api.add_resource(
        TransactionRetrieveUpdateDestroy,
        '/users/<int:user_id>/accounts/<int:account_id>/transactions/<int:transaction_id>'
    )
