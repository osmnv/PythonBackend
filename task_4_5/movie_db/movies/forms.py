
from django import forms

from .models import Movie, Review


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('user_id', 'text')


class AddMovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
