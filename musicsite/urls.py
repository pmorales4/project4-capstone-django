
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='music-home'),
    path('about', views.about, name='music-about'),
    path('musician', views.musician, name='music-musician')


    # path('', views.artist_list, name= 'artist_list'),
    # path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    # path('artist/new/', views.artist_create, name='artist_create'),
    # path('artist/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    # path('artist/<int:pk>/delete/', views.artist_delete, name='artist_delete'),


]
