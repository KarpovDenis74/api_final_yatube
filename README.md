# api_final

API для проекта Yatube

Документация запросов API находится по адресу api/templates/redoc.html
    - аутентификацию по JWT-токену
    - используется rest_framework

Запуск 
1. Сказать репозиторий 
    git clone ...
2. Создать вируальное окружение
    python -m venv venv
3. Запустить виртуальное окружение
    - для Windows
        source venv/Scripts/activate
    - для Mac и Linux
        source venv/bin/activate
4. Установить зависимости
    pip install -r requirements.txt
5. Запустить сервер Django 
    python manage.py runserver
6. Сделать и запустить миграции
    python manage.py makemigrations
    python manage.py migrate
7. Создать суперпользователя
    python manage.py createsuperuser

P.S.
Комментарии, пожалуйста, присылайте по адресу fotokarpov@yandex.ru