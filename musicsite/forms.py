from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('artist_name', 'detail_picture', 'artist_genre', 'artist_email', 'artist_location',
                  'artist_social', 'artist_website', 'detail_company', 'detail_membership', 'artist_bio')
