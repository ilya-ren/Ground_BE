# Generated by Django 4.1.2 on 2024-01-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_remove_artista_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artista',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]