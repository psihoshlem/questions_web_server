import requests
import json
import datetime

from sqlalchemy.orm import sessionmaker

from db_functions.models import Question, engine

type_QuestionFromAPI = dict[str, int | str | dict[str, str]]
type_QuestionFromDB = dict[str, str | int]

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def write_questions(questions_count: int) -> None:
    for _ in range(questions_count):
        while True:
            question = get_new_question()
            if not is_question_exist(question["id"]):
                break
        write_question(question)

def write_question(question: type_QuestionFromAPI) -> None:
    with session() as db:
        new_question = Question(
            second_id=question["id"],
            answer=question["answer"],
            question=question["question"],
            value=question["value"],
            created_at=datetime.datetime.strptime(
                question["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ), 
            category_id=question["category_id"],
            category_title=question["category"]["title"]
        )
        db.add(new_question)
        db.commit()


def get_last_question() -> type_QuestionFromDB:
    with session() as db:
        last_question = db.query(Question).order_by(Question.id.desc()).first()
    if last_question:
        return {
            "id": last_question.second_id,
            "answer": last_question.answer,
            "question": last_question.question,
            "value": last_question.value,
            "created_at": str(last_question.created_at),
            "category_id": last_question.category_id,
            "category_title": last_question.category_title
        }
    return {}

def get_new_question() -> type_QuestionFromAPI:
    return json.loads(
        requests.get("https://jservice.io/api/random?count=1").text
    )[0]


def is_question_exist(id: int) -> bool:
    with session() as db:
        questions: list[Question] = db.query(Question).filter(
            Question.second_id == id
        ).all()
    return len(questions) != 0 

if __name__ == "__main__":
    print(get_last_question())
    write_questions(2)