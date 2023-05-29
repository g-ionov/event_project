# Event project
Тестовое задание для СПБ ГБУ

Для запуска проекта необходимо наличие Docker.
Чтобы запустить проект нужно выполнить следующие команды:
```
git clone https://github.com/g-ionov/event_project.git
cd event_project
docker-compose build
docker-compose up
```
При первом запуске необходимо выполнить следующие команды:
```
docker-compose run --rm web-app sh -c "python manage.py makemigrations"
docker-compose run --rm web-app sh -c "python manage.py migrate"
docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
```

Чтобы не писать такие длинные команды, можно воспользоваться терминалом сервиса web-app внутри Docker Desctop.
В таком случае, команды будут выглядеть следующим образом:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

В дополнение к основному заданию был добавлен Docker, Docker-Compose, а также автодокументация API по адресу 'api/v1/swagger'
