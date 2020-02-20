"""music_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# default views from django
from django.contrib.auth import views as auth_views
from musicusers import views as musicuser_views

from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicsite.urls')),
    path('register/', musicuser_views.register, name='register' ),
    path('profile/', musicuser_views.profile, name='profile' ),
    # default views from django
    path('login/', auth_views.LoginView.as_view(template_name='musicusers/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='musicusers/logout.html'), name='logout' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 