from django.db import models

# Create your models here.
class user(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=100, default="")
    content = models.TextField()
    date = models.DateTimeField(default=None)
    image = models.ImageField(upload_to='images/', null= True, blank = True)
    
    def __str__(self):
        return self.title

class comunidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.descripcion

