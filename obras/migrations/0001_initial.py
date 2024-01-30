# Generated by Django 4.1.2 on 2024-01-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id_obra', models.AutoField(db_column='id_obra', primary_key=True, serialize=False)),
                ('artista', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('material', models.CharField(blank=True, max_length=20, null=True)),
                ('tecnica', models.CharField(blank=True, max_length=20, null=True)),
                ('tamaño', models.IntegerField(blank=True, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('pedido', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=5, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Digital', 'Digital'), ('Tradicional', 'Tradicional'), ('Escultura', 'Escultura'), ('Fotografia', 'Fotografia')], max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='obras_imagenes/')),
            ],
        ),
    ]
