# Generated by Django 4.1.2 on 2024-01-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=25, null=True)),
                ('first_name', models.CharField(max_length=25, null=True)),
                ('last_name', models.CharField(max_length=25, null=True)),
                ('ap_materno', models.CharField(max_length=25, null=True)),
                ('fecha_nac', models.DateField(null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('region', models.CharField(max_length=20, null=True)),
                ('ciudad', models.CharField(max_length=20, null=True)),
                ('comuna', models.CharField(max_length=20, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('bio', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='galeria_art')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='artistas', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='artistas', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]