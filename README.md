[![Newspaper app workflow](https://github.com/ZubovEvgeniy/newspaper/actions/workflows/newspaper_workflow.yml/badge.svg)](https://github.com/ZubovEvgeniy/newspaper/actions/workflows/newspaper_workflow.yml)
# Newspaper - новостной сервис

## Описание
Сервис для публикации новостей и комментирования с возможностью поставить "Like" понравившейся новости. 

Присоединяйся!

## API Reference
Сервис доступен по адресу [http://45.9.40.154/](http://45.9.40.154/)

Для взаимодействия с сервисом отправьте запросы:

**POST** http://45.9.40.154/auth/users/

> Зарегистрировать нового пользователя
> В теле запроса передать username  и password

**POST** http://45.9.40.154/auth/jwt/create/

> Получить токен пользователя
> В теле запроса передать username  и password

**GET** http://45.9.40.154/news_api/v1/news/

> Получить список новостей
> Для пагинации добавить к запросу ?limit=2&offset=4/
> Такой GET-запрос вернёт два объекта, с пятого по шестой

**GET** http://45.9.40.154/news_api/v1/news/<int:pk>/

Получить новость

**POST** http://45.9.40.154/news_api/v1/news/

> Опубликовать новость
> В теле запроса передать name  и text

**PUT** http://45.9.40.154/news_api/v1/news/<int:pk>/

> Отредактировать новость
> В теле запроса передать name  и text

**DELETE** http://45.9.40.154/news_api/v1/news/<int:pk>/

> Удалить новость

**GET** http://45.9.40.154/news_api/v1/news/<int:pk>/comments/

> Получить список комментариев к новости
> Для пагинации добавить к запросу ?limit=2&offset=4/
> Такой GET-запрос вернёт два объекта, с пятого по шестой

**GET** http://45.9.40.154/news_api/v1/news/<int:pk>/comments/<int:pk>/

> Получить комментарий к новости

**POST** http://45.9.40.154/news_api/v1/news/<int:pk>/comments/

> Опубликовать комментарий к новости

**DELETE** http://45.9.40.154/news_api/v1/news/<int:pk>/comments/<int:pk>/

> Удалить комментарий к новости

**POST** http://45.9.40.154/news_api/v1/news/<int:pk>/like/

> Поставить новости лайк

**POST** http://45.9.40.154/news_api/v1/news/<int:pk>/dislike/

> Убрать лайк

## Подготовка и запуск проекта
##### Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone git@github.com:ZubovEvgeniy/newspaper.git
```

## Установка на удаленном сервере (Ubuntu):
##### Шаг 1. Выполните вход на свой удаленный сервер
Прежде, чем приступать к работе, необходимо выполнить вход на свой удаленный сервер:
```bash
ssh <USERNAME>@<IP_ADDRESS>
```

##### Шаг 2. Установите docker на сервер:
Введите команду:
```bash
sudo apt install docker.io 
```

##### Шаг 3. Установите docker-compose на сервер:
Введите команды:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

##### Шаг 4. Локально отредактируйте файл nginx.conf
Локально отредактируйте файл `nginx/default.conf` и в строке `server_name` впишите свой IP.

##### Шаг 5. Скопируйте подготовленные файлы из каталога infra:
Скопируйте подготовленные файлы `docker-compose.yml` и `nginx/default.conf` из вашего проекта на сервер в `home/<ваш_username>/docker-compose.yml` и `home/<ваш_username>/default.conf` соответственно.
Введите команду из корневой папки проекта:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/default.conf
```

##### Шаг 6. Cоздайте .env файл:
На сервере создайте файл `nano .env` и заполните переменные окружения (или создайте этот файл локально и скопируйте файл по аналогии с предыдущим шагом):
```bash
SECRET_KEY=<SECRET_KEY>
DEBUG=<True/False>

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

##### Шаг 7. Добавьте Secrets:
Для работы с Workflow добавьте в Secrets GitHub переменные окружения для работы:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

DOCKER_PASSWORD=<пароль DockerHub>
DOCKER_USERNAME=<имя пользователя DockerHub>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<ID своего телеграм-аккаунта>
TELEGRAM_TOKEN=<токен вашего бота>
```

##### Шаг 8. Запуск GitHub Actions:
Зайдите на боевой сервер и выполните команды:
```bash
git add .
git commit -m 'your commit name'
git push
```
GitHub Actions запустится в автоматическом режиме
 
```
###### Заполнить базу данных:
```bash
sudo docker-compose exec backend python manage.py load_data
```
##### Шаг 9. Создать суперпользователя Django:
```bash
sudo docker-compose exec <newspapers-id> python manage.py createsuperuser
```

**Проект будет доступен по вашему IP-адресу.**
**Логин суперпользователя:** superuser
**Пароль:** Qwerty1234!


**Автор**
Евгений Зубов
2023
