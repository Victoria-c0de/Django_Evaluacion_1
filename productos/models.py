from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, default="Valor Predeterminado")
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.CharField(max_length=50, blank=True)

def __str__(self):
        return self.nombre