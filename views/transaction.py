from pydantic import BaseModel, PositiveFloat
from pydantic import AwareDatetime, NaiveDatetime


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    timestamp: AwareDatetime | NaiveDatetime
