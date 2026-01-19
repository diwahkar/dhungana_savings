from typing import Annotated

from fastapi import Query

from index import app
from models import MonthlyAmounts, MonthlyAmountPost
from sqlmodel import Session, select
from db_config import engine



@app.get('/monthlyamounts')
def get_monthlyamounts(offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(MonthlyAmounts).offset(offset).limit(limit)
    with Session(engine) as session:
        monthlyamounts = session.exec(statement).all()
    return [monthlyamount.model_dump() for monthlyamount in monthlyamounts]


@app.get('/monthlyamounts/{monthlyamount_id}')
def get_monthlyamount(monthlyamount_id: int):
    statement = select(MonthlyAmounts).where(MonthlyAmounts.id==monthlyamount_id)
    with Session(engine) as session:
        monthlyamount = session.exec(statement).first()
        if monthlyamount is None:
            return 'monthlyamount not found'

        return monthlyamount.model_dump()


@app.post('/monthlyamounts')
def create_monthlyamount(requestBody: MonthlyAmountPost):
    requestBody = requestBody.model_dump()
    monthlyamount = MonthlyAmounts()
    for key, value in requestBody.items():
        if key in monthlyamount.model_fields:
            setattr(monthlyamount, key, value)

    with Session(engine) as session:
        session.add(monthlyamount)
        session.commit()
        session.refresh(monthlyamount)
    return monthlyamount.id


@app.put('/monthlyamounts/{monthlyamount_id}')
def update_monthlyamount(monthlyamount_id: int, reqeustBody: MonthlyAmountPost):
    statement = select(MonthlyAmounts).where(MonthlyAmounts.id==monthlyamount_id)
    with Session(engine) as session:
        monthlyamount = session.exec(statement).first()
        if monthlyamount is None:
            return 'monthlyamount not found'

        reqeustBody = reqeustBody.model_dump()
        for key, value in reqeustBody.items():
            if key in monthlyamount.model_fields:
                setattr(monthlyamount, key, value)

            session.add(monthlyamount)
            session.commit()
            session.refresh(monthlyamount)
        return monthlyamount.id


@app.delete('/monthlyamounts/{monthlyamount_id}')
def delete_monthlyamount(monthlyamount_id: int):
    statement = select(MonthlyAmounts).where(MonthlyAmounts.id==monthlyamount_id)
    with Session(engine) as session:
        monthlyamount = session.exec(statement).first()
        if monthlyamount is None:
            return 'monthlyamount not found'

        session.delete(monthlyamount)
        session.commit()
        return 'monthlyamount Deleted'


@app.get('/monthlyamounts/username/{username}')
def get_monthlyamounts_by_username(username: str, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(MonthlyAmounts).where(MonthlyAmounts.member_name==username)
    with Session(engine) as session:
        monthlyamounts = session.exec(statement).all()
        return [ monthlyamount.model_dump() if monthlyamounts else '' for monthlyamount in monthlyamounts]
