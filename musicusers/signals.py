# fires when a user gets created/saved.
from django.db.models.signals import post_save 
# post saved signal - User is the sending - sends signal
from django.contrib.auth.models import User 
# gets the signal - receiver - performs some task 
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save() 