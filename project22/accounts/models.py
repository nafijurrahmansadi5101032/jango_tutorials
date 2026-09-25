from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.name
