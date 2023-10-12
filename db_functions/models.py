from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///marketplace.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)
    created_at = Column(DATETIME)
    category_id = Column(Integer)
    category_title = Column(String)

Base.metadata.create_all(bind=engine)
