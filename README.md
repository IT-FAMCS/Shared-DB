## Копируете файлы urls.py, views.py, serializer.py, меняя все под нужное приложение

# НЕ ТРОГАТЬ USERS, а так же модели

```
ssh-keygen -t rsa -C "ВАША ПОЧТА"
```

переходите в C:/Users/ПОЛЬЗОВАТЕЛЬ/.ssh берете оттуда id_rsa.pub, копируете и добавляете в ваш GitHub Настройки > SSH and GPG keys > New SSH Key и вставляете ключ

## Чтобы скопировать репозиторий вводим следующий промпт

```
git clone git@github.com:essaon/Shared-BD.git
```

## комманды:

```
git add -A
git push - добавить новые изменения
git pull - получить новые изменения
git checkout -b - создать и перейти в ветку
```

## Скачать зависимости

```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
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
