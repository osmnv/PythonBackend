
from django.contrib import admin
from django.urls import include, path

from . import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.index),
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls'))
]
