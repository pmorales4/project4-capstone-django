
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='music-home'),
    path('about', views.about, name='music-about'),
    path('musician', views.musician, name='music-musician'),
    path('dumpartist', views.dumpartist, name='music-dumpartist')



]
