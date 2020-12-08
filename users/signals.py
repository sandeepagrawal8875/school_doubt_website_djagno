from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from users.models import Profile

def Userprofile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance, name=instance.username)

post_save.connect(Userprofile, sender=User)