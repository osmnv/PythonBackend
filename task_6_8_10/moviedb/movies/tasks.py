
from django.core.mail import send_mail
from django.utils import timezone
from celery import shared_task

from application import settings


@shared_task()
def new_movie(movie_title, staff_member):
    send_mail(
        subject='MovieDB notification',
        message=f'New movie {movie_title} added by {staff_member}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.ADMIN_EMAIL],
    )

@shared_task
def simple_task():
    with open(settings.CELERY_LOG_FILE, 'a') as f:
        f.write(f'{timezone.now()}: 42\n')