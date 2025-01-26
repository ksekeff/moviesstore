from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Modo como é chamado a url de app home
    path('movies/', include('movies.urls')), # Modo como é chamado a url de app movies
    path('accounts/', include('accounts.urls')), # Modo como é chamado a url de app accounts
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

