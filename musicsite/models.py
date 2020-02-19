from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_genre = models.CharField(max_length=50)
    artist_email = models.CharField(max_length=100)
    artist_location = models.CharField(max_length=100)
    artist_social = models.CharField(max_length=100)
    artist_website = models.CharField(max_length=100)
    artist_bio = models.TextField()
  
    def __str__(self):
       return self.artist_name 

class Detail(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='details')
    detail_company = models.CharField(max_length=100, default='Enter Company Representative')
    detail_membership = models.CharField(max_length=100, default='Enter Membership Group')
    detail_picture = models.ImageField(upload_to='artist/picture/', null=True, blank=True)

    def __str__(self):
        return self.detail_company 

   
 