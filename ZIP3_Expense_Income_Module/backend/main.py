
from fastapi import FastAPI
from routers.expense import router as expense_router
from routers.income import router as income_router

app = FastAPI(title='Expense AI System')

app.include_router(expense_router)
app.include_router(income_router)

@app.get('/')
def home():
    return {'message':'Expense & Income Module Running'}
