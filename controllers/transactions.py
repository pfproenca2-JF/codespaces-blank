from fastapi import APIRouter, Depends, status

from schemas.transaction import TransactionIn
from security import login_required
from services.transaction import TransactionService
from views.transaction import TransactionOut

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
	return await service.create(transaction)