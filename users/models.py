from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} Profile'
