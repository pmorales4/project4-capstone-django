from django.db import models
# added one line below for user


# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=100, default='Enter Name')
    detail_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    artist_genre = models.CharField(max_length=50, default='Enter Genre')
    artist_email = models.CharField(max_length=100, default='Enter Email')
    artist_location = models.CharField(max_length=100, default='Where Are You Located')
    artist_social = models.CharField(max_length=100, default='Enter Primary Social Network')
    artist_website = models.CharField(max_length=100, default='Enter Personal Website')
    detail_company = models.CharField(max_length=100, default='Enter Company Representative')
    detail_membership = models.CharField(max_length=100, default='Enter Membership Group')
    artist_bio = models.TextField()
  
    def __str__(self):
       return self.artist_name 



   
 