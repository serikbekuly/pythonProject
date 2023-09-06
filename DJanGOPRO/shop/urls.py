from django.urls import path
from . import views
from DJanGOPRO import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('go', views.go, name="go"),
    path('domashka', views.domashka, name="domashka" )
]