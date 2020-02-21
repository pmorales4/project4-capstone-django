from django.urls import path

from musicsite import views as musicsite_views


urlpatterns = [
    path('', musicsite_views.home, name='music-home')
]