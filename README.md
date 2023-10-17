# questions_web_server

Данный проект разработан в качестве тестового задания на вакансию Python разработчик (Junior).

## Запуск с докером

Так же Вы можете запустить наш сервис с помощью докера:
```bash
$ git clone https://github.com/psihoshlem/questions_web_server.git
$ cd questions_web_server
$ docker-compose up -d
```
Для использования советую использовать swagger ui.  Для этого после запуска проекта перейдите по ссылке http://127.0.0.1:8000/docs.

## Пример запроса
```bash
curl -X 'POST' \
  'http://localhost:8000/get_question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 2
}'
```
Пример ответа:
```bash
{
  "id": 81306,
  "answer": "an artichoke",
  "question": "A sunchoke is also called a Jerusalem one of these",
  "value": 1000,
  "created_at": "2022-12-30 19:13:59.621000",
  "category_id": 7221,
  "category_title": "eat your veggies"
}
```
