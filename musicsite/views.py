from django.shortcuts import render
from .models import Artist, Detail

# Create your views here.
# logic for routes in this page

def home(request):
    artists = Artist.objects.all()
    return render(request, 'musicsite/home.html', {'artists': artists})

def about(request):
    return render(request, 'musicsite/about.html')
    