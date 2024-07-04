from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QuestionsAndAnswers(Base):
    __tablename__ = 'questions_and_answers'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
