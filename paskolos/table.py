from sqlalchemy import Column, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///loans.db')
Base = declarative_base()

class Loans(Base):
    __tablename__ = 'Loans'
    id = Column(Integer, primary_key=True)
    amount = Column("Amount", Integer)
    period = Column("Period", Integer)
    interest = Column("Interest", Float)

    def __init__(self, amount, period, interest):
        self.amount = amount
        self.period = period
        self.interest = interest

    def __repr__(self):
        return f"{self.id} - Amount: {self.amount}, Period: {self.period}, Interest: {self.interest}"

Base.metadata.create_all(engine)