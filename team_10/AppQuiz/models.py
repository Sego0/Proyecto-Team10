from django.db import models

class pregunta(models.Model):
    texto= models.TextField(verbose_name="Pregunta")
    def __str__(self):
        return self.texto
class EleccionRespuesta(models.Model):
    pregunta=models.ForeignKey(pregunta, related_name="preguntas", on_delete=models.CASCADE)
    correcta=models.BooleanField(verbase_name="Es la correcta", default=False, null=False)
    texto=models.TextField(verbose_name="Texto de la respuesta")
# Create your models here.
