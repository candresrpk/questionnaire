from django.contrib import admin
from .models import Encuesta, Pregunta, Opcion, Respuesta
# Register your models here.


@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('encuesta', 'status')
    list_filter = ('status',)
    search_fields = ('encuesta',)
    prepopulated_fields = {'encuesta': ('encuesta',)}


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'encuesta')
    list_filter = ('encuesta',)
    search_fields = ('pregunta',)


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ('opcion', 'pregunta')
    list_filter = ('pregunta',)
    search_fields = ('opcion',)


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('encuesta', 'pregunta', 'opcion')
    list_filter = ('encuesta', 'pregunta', 'opcion')
    search_fields = ('encuesta', 'pregunta', 'opcion')
