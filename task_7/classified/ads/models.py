
from django.db import models
from django.core import exceptions
from django.core.validators import MinValueValidator

import re


def PhoneNumberValidator(value):
    PATTERN = re.compile(r'^(\+7|7|8)9\d{9}$')
    if not PATTERN.match(value):
        raise exceptions.ValidationError('Invalid phone number')


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [PhoneNumberValidator]
        kwargs['max_length'] = 12
        super().__init__(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(null=True, max_length=20)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='parent category'
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        if self.parent == None:
            return self.title
        else:
            return str(self.parent) + " - " + self.title


class Ad(models.Model):
    title = models.CharField(max_length=30)
    descr = models.CharField(max_length=100, verbose_name='decription')
    phone_num = PhoneNumberField(verbose_name='contact phone number')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='publication date')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="ad's category"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )

    class Meta:
        ordering = ['pub_date']
        indexes = [
            models.Index(fields=['pub_date'], name='pub_date_idx'),
            models.Index(fields=['price'], name='price_idx'),
        ]

    def __str__(self):
        return f"{self.title} ({self.pub_date.strftime('%d.%m.%Y %H:%M')})"
