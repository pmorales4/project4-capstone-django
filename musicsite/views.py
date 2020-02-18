from django.shortcuts import render


# Create your views here.
# logic for routes in this page

def home(request):
    return render(request, 'musicsite/base.html')

def about(request):
    return render(request, 'musicsite/about.html')
    