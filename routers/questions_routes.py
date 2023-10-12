from pydantic import BaseModel
from fastapi import APIRouter

from db_functions.questions_funcs import write_questions, get_last_question

class QuestionsInfo(BaseModel):
    questions_num: int

router = APIRouter()

@router.post("/get_question", tags=["questions"])
async def get_question_and_write_new(questions_info: QuestionsInfo):
    question = get_last_question()
    write_questions(questions_info.questions_num)
    return question