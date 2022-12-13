# Django intensive
![project workflow](https://github.com/visill/group_project/actions/workflows/python-app.yml/badge.svg)
![project workflow](https://github.com/visill/group_project/actions/workflows/django.yml/badge.svg)
## Quickstart
1. Скачиваем, заходим в папку проекта

2. Если нет virtualenv устанавливаем
`pip3 install virtualenv`
3. Создаем окружение
`virtualenv venv`   
4. Входим в виртуальное окружение
`source venv/bin/activate`   
5. Создаем файл .env, подобный .env.example, заполняем критичную информацию
6. Установливаем зависимости
`pip3 install -r requirements.txt`
7. Запускаем миграции
`python3 manage.py migrate`
8. Запускаем сервер
`python3 manage.py runserver`
9. Готово! Сайт доступен по адресу http://127.0.0.1:8000/
