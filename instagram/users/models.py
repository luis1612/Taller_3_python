from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	biografia = models.TextField(blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	foto = models.ImageField(upload_to='users/fotos', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


