from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,Boolean

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String,unique=True, index=True)
    password = Column(String)
    address = Column(String) 
    phone = Column(String)
    isprime= Column(Boolean,default=False)
    