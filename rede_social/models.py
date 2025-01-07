from django.db import models
#from datetime import datetime
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=16, unique=True, blank=False, primary_key=True)
    email = models.EmailField(max_length=30, unique=True, blank=False)
    # password = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank = False, null = True)
    data_criacao = models.DateField(null = True, auto_now_add=True)
    foto_perfil = models.ImageField(null = True, blank=True, upload_to='users_profile_picture/')

    def __str__(self):
        return self.username

class Postagem(models.Model):
    texto = models.TextField(null=False, blank=False, max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True, blank=False)
    imagem = models.ImageField(null = True, upload_to='posts/')

    def __str__(self):
        return self.texto

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete = models.CASCADE)
    comentario = models.TextField(max_length=100, null=False, blank=False)
    data_hora = models.DateTimeField(auto_now_add=True, blank=False, null=True)

