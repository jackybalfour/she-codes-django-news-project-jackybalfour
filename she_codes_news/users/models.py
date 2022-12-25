from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


# class profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #image
#     def __str__(self):
#         return f'Hello {self.user.username}, welcome to your profile'
    
# Create your models here.
