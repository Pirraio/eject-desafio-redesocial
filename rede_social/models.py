from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Postagens(models.Model):
    pass

class Comentarios(models.Model):
    pass
