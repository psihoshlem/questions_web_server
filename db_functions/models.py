from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/questions"
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
