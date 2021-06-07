
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True ,verbose_name='personal info')
    joined_at = models.DateField(auto_now_add=True, verbose_name='date user joined')

    def __str__(self):
        return self.username
