
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required as staff

from . import views
from users.views import my_login_required as login

app_name = 'movies'

urlpatterns = [
    path('', views.MovieIndexView.as_view(), name='movies_index'),
    path('add', staff(views.MovieAddView.as_view()), name='add_movie'),
    path('<int:pk>', views.MovieDetailView.as_view(), name='movie_details'),
    path('<int:pk>/edit', staff(views.MovieEditView.as_view()), name='edit_movie'),
    path('<int:pk>/delete', staff(views.MovieDeleteView.as_view()), name='delete_movie'),
    path('<int:pk>/add_review', login(views.ReviewAddView.as_view()), name='add_review')
]
