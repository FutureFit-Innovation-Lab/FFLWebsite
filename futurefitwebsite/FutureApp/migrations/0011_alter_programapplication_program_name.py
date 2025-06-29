# Generated by Django 5.2 on 2025-06-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutureApp', '0010_programapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programapplication',
            name='program_name',
            field=models.CharField(choices=[('AI_ML', 'Artificial Intelligence (AI) and Machine Learning (ML) Essentials'), ('EMBEDDED', 'Embedded System'), ('3D_PRINT', '3D Design and Printing'), ('PYTHON_DJANGO', 'Python and Django enabled web application for content management')], max_length=50),
        ),
    ]
