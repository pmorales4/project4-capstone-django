from django.db import models
# added one line below for user


# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=100,)
    detail_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    artist_genre = models.CharField(max_length=50,)
    artist_email = models.CharField(max_length=100,)
    artist_location = models.CharField(max_length=100,)
    artist_social = models.CharField(max_length=100,)
    artist_website = models.CharField(max_length=100,)
    detail_company = models.CharField(max_length=100,)
    detail_membership = models.CharField(max_length=100,)
    artist_bio = models.TextField()

    # objects = models.Manager()
  
    def __str__(self):
       return self.artist_name 



   
 