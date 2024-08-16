from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Create your models here.
