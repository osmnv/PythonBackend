
from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Genre(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "genres"

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=30)
    rel_date = models.DateField(verbose_name='release date')
    producer = models.CharField(max_length=30)
    descr = models.TextField(verbose_name='description')
    genres = models.ManyToManyField(Genre, verbose_name='related genres')
    poster = models.ImageField(upload_to='movie_posters/',
                               default='movie_posters/no-poster.jpg')
    users_reviews = models.ManyToManyField(
        CustomUser,
        through='Review',
        through_fields=('movie', 'user')
    )

    class Meta:
        ordering = ['rel_date']
        indexes = [
            models.Index(fields=['rel_date'], name='rel_date_idx'),
        ]
        verbose_name_plural = "movies"
    
    def get_absolute_url(self):
        return reverse('movies:movie_details', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title} ({self.rel_date.year})'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True, verbose_name='date published')
    text = models.TextField(verbose_name='review text')

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f"{self.user} on {self.movie}"
