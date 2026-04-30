from django.db import models

class Userprofile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255) # Longer for hashing
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username