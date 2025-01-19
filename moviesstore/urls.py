from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Modo como é chamado a url de app home
    path('movies/', include('movies.urls')), # Modo como é chamado a url de app movies
]

