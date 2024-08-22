# Запуск на Windows

## Создать вирутальное окружение

```
python -m venv venv
venv/Scripts/activate
```

## Загрузить библиотеки

```
python -m pip install -r requirements.txt
```

## Выполнить миграции

```
python manage.py makemigraions
python manage.py migrate
```

## Запустить сервер

```
python manage.py runserver
```

# Запуск на MacOS

## Создать в корневой папке папку с именем base

```
mkdir base
```

## Создать вирутальное окружение

```
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
```

## Загрузить библиотеки

```
python3 -m pip install -r requirements.txt
```

## Выполнить миграции

```
python3 manage.py makemigraions
python3 manage.py migrate
```

## Запустить сервер

```
python3 manage.py runserver
```

# ОНЛИ ДЛЯ ДЕПЛОЯ

## Устанавливаем ssh ключи в свой гитхаб

```
ssh-keygen -t rsa -C "ВАША ПОЧТА"
```

переходите в C:/Users/ПОЛЬЗОВАТЕЛЬ/.ssh берете оттуда id_rsa.pub, копируете и добавляете в ваш GitHub Настройки > SSH and GPG keys > New SSH Key и вставляете ключ

## Копируем репозиторий

```
git clone git@github.com:essaon/Shared-BD.git
```

## Закидываем файл setup.py на один уровень с manage.py

    Запускаем файл и выполняем все условия

## Устанавливаем все нужные библиотеки

```
python3 -m pip install djangorestframework django jwt PyJWT celery
```

## Запустить сервер Django

```
python3 manage.py runserver
```

## Запустить услуги Celery

```
celery --app=BD worker --loglevel=info --pool=solo
celery -A BD beat -l info
```
