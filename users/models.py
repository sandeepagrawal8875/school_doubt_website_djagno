from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):

    GENDER_CHOICES = (
        ('male','male'),
        ('female','female'),
        ('other','other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False,default="")
    image = models.ImageField(upload_to='image/',default='default.png', null=True, blank=True)
    field = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=51, null=True, blank=True)
    location = models.CharField(max_length=200,null=True)
    about = models.CharField(max_length=300,null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50,null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'