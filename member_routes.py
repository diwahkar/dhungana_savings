from typing import Annotated

from fastapi import FastAPI, Query

from models import Members, MemberPost
from sqlmodel import Session, select
from db_config import engine


app = FastAPI()


@app.get('/members')
def get_members(offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(Members).offset(offset).limit(limit)
    with Session(engine) as session:
        members = session.exec(statement).all()
    return [member.model_dump() for member in members]


@app.get('/members/{member_id}')
def get_member(member_id: int):
    statement = select(Members).where(Members.id==member_id)
    with Session(engine) as session:
        member = session.exec(statement).first()
        if member is None:
            return 'Member not found'

        return member.model_dump()


@app.post('/members')
def create_member(requestBody: MemberPost):
    requestBody = requestBody.model_dump()
    member = Members(name=requestBody['name'])
    with Session(engine) as session:
        session.add(member)
        session.commit()
        session.refresh(member)
    return member.id


@app.put('/members/{member_id}')
def upate_member(member_id: int, member_update: MemberPost):
    statement = select(Members).where(Members.id==member_id)
    with Session(engine) as session:
        member = session.exec(statement).first()
        if member is None:
            return 'Member not found'

        member_update = member_update.model_dump()
        for key, value in member_update.items():
            if key in member.model_fields:
                setattr(member, key, value)

            session.add(member)
            session.commit()
            session.refresh(member)
        return member.id


@app.delete('/members/{member_id}')
def delete_member(member_id: int):
    statement = select(Members).where(Members.id==member_id)
    with Session(engine) as session:
        member = session.exec(statement).first()
        if member is None:
            return 'Member not found'

        session.delete(member)
        session.commit()
        return 'Member Deleted'
