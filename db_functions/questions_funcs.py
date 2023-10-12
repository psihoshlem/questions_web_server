import requests
import json

def write_questions(questions_count):
    for num_question in questions_count:
        question = get_new_question()
        if is_question_exist(question):
            write_questions(question)

def write_question():
    pass


def get_last_question():
    pass

def get_new_question():
    return json.loads(
        requests.get("https://jservice.io/api/random?count=1").text
    )[0]


def is_question_exist():
    pass

if __name__ == "__main__":
    get_new_question()