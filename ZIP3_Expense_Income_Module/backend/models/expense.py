
from sqlalchemy import Column,Integer,String,ForeignKey
from models.user import Base

class Expense(Base):
    __tablename__='expenses'

    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer)
    category = Column(String)
    merchant = Column(String)
    description = Column(String)
