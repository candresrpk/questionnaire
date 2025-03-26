from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Encuesta(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='encuestas')
    encuesta = models.CharField(max_length=200)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT
                              )

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __str__(self):
        return self.encuesta


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    encuesta = models.ForeignKey(
        Encuesta, on_delete=models.CASCADE, related_name='preguntas')

    def __str__(self):
        return self.pregunta


class Opcion(models.Model):

    class Categoria(models.TextChoices):
        MULTICHOICES = 'MC', 'Multichoice'
        OPEN = 'OP', 'Open'
        SINGLECHOICE = 'SC', 'Singlechoice'

    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.CASCADE, related_name='opciones')

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    opcion = models.CharField(max_length=200)
    categoria = models.CharField(
        max_length=200, choices=Categoria.choices, default=Categoria.SINGLECHOICE)

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Opcion'
        verbose_name_plural = 'Opciones'

    def __str__(self):
        return self.opcion


class Respuesta(models.Model):
    encuesta = models.ForeignKey(
        Encuesta, on_delete=models.PROTECT, related_name='encuestas')

    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.PROTECT, related_name='preguntas')

    opcion = models.ForeignKey(
        Opcion, on_delete=models.PROTECT, related_name='opciones')

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return f'{self.encuesta} - {self.pregunta} - {self.opcion.categoria}'
