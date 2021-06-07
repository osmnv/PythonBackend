
from django.db import models

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=50)
    rel_date = models.DateField(verbose_name='Release Date')
    producer = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} ({self.rel_date.year})'


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user_id} ({self.date}): {self.text}'
