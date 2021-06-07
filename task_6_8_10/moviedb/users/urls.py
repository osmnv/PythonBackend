
from django.urls import path

from . import views
from .views import my_login_required as login


app_name = 'users'

urlpatterns = [
    path('', views.UsersIndexView.as_view(), name='users_index'),
    path('login', views.login, name='login'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user_details'),
    path('<int:pk>/reviews', login(views.UserReviewsView.as_view()), name='user_reviews')
]