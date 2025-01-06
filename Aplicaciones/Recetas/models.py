from django.db import models

class Receta(models.Model):
    NIVEL_DIFICULTAD_CHOICES = [
        ('Fácil', 'Fácil'),
        ('Intermedio', 'Intermedio'),
        ('Difícil', 'Difícil'),
    ]

    nombre = models.CharField(max_length=255, verbose_name="Nombre de la receta")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    ingredientes = models.TextField(verbose_name="Ingredientes")
    instrucciones = models.TextField(verbose_name="Instrucciones")
    tiempo_preparacion = models.PositiveIntegerField(verbose_name="Tiempo de preparación (minutos)")
    nivel_dificultad = models.CharField(
        max_length=50,
        choices=NIVEL_DIFICULTAD_CHOICES,
        verbose_name="Nivel de dificultad"
    )
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True, verbose_name="Imagen de la receta")
    es_favorita = models.BooleanField(default=False, verbose_name="Es favorita")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")




class Comentario(models.Model):
    autor = models.CharField(max_length=100) 
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion=models.TextField()
    idioma=models.CharField(max_length=50)
    fecha_caducidad=models.DateField()
    creador=models.CharField(max_length=255)
