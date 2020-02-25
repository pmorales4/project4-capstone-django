from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseForbidden

# Create your views here.
# logic for routes in this page

def home(request):
    artists = Artist.objects.all()
    return render(request, 'musicsite/home.html', {'artists': artists})

def about(request):
    return render(request, 'musicsite/about.html')

def musician(request):
    artists = Artist.objects.all()
    return render(request, 'musicsite/musician.html', {'artists': artists})

# Artist listed out to screen
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'musicsite/artist_list.html', {'artists': artists})

# Artist detail page
def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'musicsite/artist_detail.html', {'artist': artist})
    
# CREATE AN ARTIST ON FRONT END SECTION 
# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, request.FILES)
#         # import pdb; pdb.set_trace()
#         if form.is_valid():
#             artist =form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'musicsite/artist_form.html', {'form': form})

# Edit an artist on site 
# def artist_edit(request, pk):
#     artist = Artist.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ArtistForm(request.POST, request.FILES, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'musicsite/artist_form.html', {'form': form})


# Deletes an Artist 
def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


def artist_create(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid:
            artists = form.save()
            return redirect('artists_detail', id = artists.id)
    else:
        form = ArtistForm()
        return render(request, 'artists_form.html', {'form': form})
def artists_update(request, id):
    artists = artists.objects.get(id = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance = artists)
        if form.is_valid:
            artists = form.save()
            return redirect('artists_detail', id = artists.id)
    else:
        form = ArtistForm(instance = artists)
        return render(request, 'artists_form.html', {'form': form})