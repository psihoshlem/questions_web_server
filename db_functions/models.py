from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from db_functions.db_config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    second_id = Column(Integer)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)
    created_at = Column(TIMESTAMP)
    category_id = Column(Integer)
    category_title = Column(String)

Base.metadata.create_all(bind=engine)
