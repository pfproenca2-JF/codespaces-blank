from databases.interfaces import Record

from database import database
from exceptions import AccountNotFoundError, BusinessError
from models.account import accounts
from models.transactions import TransactionType, transactions
from schemas.transaction import TransactionIn


class TransactionService:
    async def read_all(self, account_id: int, limit: int = 100, skip: int = 0) -> list[Record]:
        query = (
            transactions.select()
            .where(transactions.c.account_id == account_id)
            .limit(limit)
            .offset(skip)
        )
        return await database.fetch_all(query)
    
    @database.transaction()
    async def create(self, transaction: TransactionIn) -> Record:
        query = accounts.select().where(accounts.c.id == transaction.account_id)
        account = await database.fetch_one(query)
        if not account:
            raise AccountNotFoundError

        if transaction.type == TransactionType.WITHDRAWAL:
            new_balance = float(account["balance"]) - float(transaction.amount)
        else:
            new_balance = float(account["balance"]) + float(transaction.amount)

        if new_balance < 0:
            raise BusinessError("Operation not carried out due to lack of balance")

        await database.execute(
            accounts.update().where(accounts.c.id == transaction.account_id).values(balance=new_balance)
        )

        tx_cmd = transactions.insert().values(
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
        )
        tx_id = await database.execute(tx_cmd)
        return await database.fetch_one(transactions.select().where(transactions.c.id == tx_id))