
from django.urls import path

from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('<int:pk>/reviews', views.reviews, name='reviews'),
    path('<int:pk>/add_review', views.add_review, name='add_review')
]