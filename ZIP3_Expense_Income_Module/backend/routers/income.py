
from fastapi import APIRouter

router = APIRouter(prefix='/income',tags=['Income'])

@router.get('/')
def get_income():
    return {'message':'Get income records'}

@router.post('/')
def add_income():
    return {'message':'Income added'}

@router.delete('/{income_id}')
def delete_income(income_id:int):
    return {'message':f'Income {income_id} deleted'}
