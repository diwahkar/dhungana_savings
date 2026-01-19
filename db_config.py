import os
from dotenv import load_dotenv

from sqlmodel import SQLModel, create_engine

import models


load_dotenv()

DATABASE = os.getenv('DATABASE', '')
USERNAME = os.getenv('USERNAME', '')
PASSWORD = os.getenv('PASSWORD', '')
HOST = os.getenv('HOST', '')
PORT = os.getenv('PORT', '')

db_url = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(db_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)
