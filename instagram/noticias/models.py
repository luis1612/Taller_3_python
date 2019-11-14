from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=255)
	foto = models.ImageField(upload_to='noticias/fotos')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
