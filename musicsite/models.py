from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_genre = models.CharField(max_length=50)
    artist_email = models.CharField(max_length=100)
    artist_location = models.CharField(max_length=100)
    artist_bio = models.TextField()
  
   
   
