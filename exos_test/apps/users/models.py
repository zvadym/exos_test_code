import random
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_random():
    return random.randint(1, 100)


class User(AbstractUser):
    birthday = models.DateField(help_text='YYYY-MM-DD')
    random_number = models.PositiveSmallIntegerField(default=get_random)
