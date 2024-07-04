
from app.models.QuestionsAndAnswers import QuestionsAndAnswers


class DBManager:

    @staticmethod
    def save_question_answer(db, question: str, answer: str) -> None:
        try:
            qa = QuestionsAndAnswers(question=question, answer=answer)
            db.session.add(qa)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Failed to save question-answer pair: {str(e)}")


    @staticmethod
    def get_answer_from_database(db, question: str) -> str:
        try:
            existing_qa = db.session.query(QuestionsAndAnswers).filter_by(question=question).first()
            if existing_qa:
                return existing_qa.answer
            return ''
        except Exception as e:
            raise Exception(f"Failed to retrieve answer from database: {str(e)}")




