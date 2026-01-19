from datetime import datetime

from sqlmodel import Field, SQLModel


class Members(SQLModel, table=True):

    id       : int | None = Field(primary_key=True) # int | None means we may or may not pass the int value to id duing Member object creation
    name     : str = Field(index=True, unique=True)


class Loans(SQLModel, table=True):

    id             : int | None = Field(primary_key=True) # int | None means we may or may not pass the int value to id duing Member object creation
    amount         : int
    date_taken     : datetime = Field(default_factory=datetime.now())
    date_returned  : datetime = Field(default=None)
    member_name    : str = Field(foreign_key='members.name')


class MonthlyAmounts(SQLModel, table=True):

    id               : int | None = Field(primary_key=True) # int | None means we may or may not pass the int value to id duing Member object creation
    monthly_saving   : int = Field(default=1000)
    loan_interest    : int | None = Field(default=None)
    date             : datetime = Field(default=None)
    member_name      : str | None = Field(foreign_key='members.name')
    loan_id          : int | None = Field(default=None, foreign_key='loans.id')
