from django.urls import path
from . import views
from DJanGOPRO import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('go', views.go, name="go"),
    path('domashka', views.domashka, name="domashka" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)