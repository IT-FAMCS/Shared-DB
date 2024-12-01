from celery import shared_task
from django.core.management import call_command

@shared_task()
def dbackup_task():
    call_command('dbackup')
    
import requests
from celery import shared_task
from django.db import connection

@shared_task
def update_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users_user")
        users = cursor.fetchall()

    users_data = [
        {desc[0]: user[i] for i, desc in enumerate(cursor.description)}
        for user in users
    ]

    response = requests.post(
        "https://legacy-famcs-stage.ru/api/users/update",
        json={"users": users_data},
    )

    return response.status_code