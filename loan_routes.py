from typing import Annotated

from fastapi import Query

from index import app
from models import Loans, LoanPost
from sqlmodel import Session, select
from db_config import engine



@app.get('/Loans')
def get_Loans(offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(Loans).offset(offset).limit(limit)
    with Session(engine) as session:
        loans = session.exec(statement).all()
    return [loan.model_dump() for loan in loans]


@app.get('/Loans/{loan_id}')
def get_loan(loan_id: int):
    statement = select(Loans).where(Loans.id==loan_id)
    with Session(engine) as session:
        loan = session.exec(statement).first()
        if loan is None:
            return 'loan not found'

        return loan.model_dump()


@app.post('/Loans')
def create_loan(requestBody: LoanPost):
    requestBody = requestBody.model_dump()
    loan = Loans()
    for key, value in requestBody.items():
        if key in loan.model_fields:
            setattr(loan, key, value)

    with Session(engine) as session:
        session.add(loan)
        session.commit()
        session.refresh(loan)
    return loan.id


@app.put('/Loans/{loan_id}')
def update_loan(loan_id: int, reqeustBody: LoanPost):
    statement = select(Loans).where(Loans.id==loan_id)
    with Session(engine) as session:
        loan = session.exec(statement).first()
        if loan is None:
            return 'loan not found'

        reqeustBody = reqeustBody.model_dump()
        for key, value in reqeustBody.items():
            if key in loan.model_fields:
                setattr(loan, key, value)

            session.add(loan)
            session.commit()
            session.refresh(loan)
        return loan.id


@app.delete('/Loans/{loan_id}')
def delete_loan(loan_id: int):
    statement = select(Loans).where(Loans.id==loan_id)
    with Session(engine) as session:
        loan = session.exec(statement).first()
        if loan is None:
            return 'loan not found'

        session.delete(loan)
        session.commit()
        return 'loan Deleted'


@app.get('/Loans/username/{username}')
def get_loan_by_username(username: str, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(Loans).where(Loans.member_name==username)
    with Session(engine) as session:
        loans = session.exec(statement).all()
        return [ loan.model_dump() if loans else '' for loan in loans]
