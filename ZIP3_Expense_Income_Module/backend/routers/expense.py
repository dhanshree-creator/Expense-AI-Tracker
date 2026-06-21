
from fastapi import APIRouter

router = APIRouter(prefix='/expenses',tags=['Expenses'])

@router.get('/')
def get_expenses():
    return {'message':'Get all expenses'}

@router.post('/')
def add_expense():
    return {'message':'Expense added'}

@router.delete('/{expense_id}')
def delete_expense(expense_id:int):
    return {'message':f'Expense {expense_id} deleted'}
