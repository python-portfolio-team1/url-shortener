from django import views
from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.home, name='home'),
    path('short', views.short, name='short'),
    path('<str:shortURL>', views.redirect_short_url, name='redirect-url')
]