from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Reserva.urls'), name='Reserva'),
    path('auth/', include('Auth_Reserva.urls'), name='auth'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)