# Generated by Django 5.1.7 on 2025-03-26 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='encuesta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='encuestas.encuesta'),
            preserve_default=False,
        ),
    ]
