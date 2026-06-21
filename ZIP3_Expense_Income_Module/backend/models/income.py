
from sqlalchemy import Column,Integer,String,ForeignKey
from models.user import Base

class Income(Base):
    __tablename__='incomes'

    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String)
    amount = Column(Integer)
