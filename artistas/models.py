from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission

#BaseUseManager, ayuda a manejar los registros de usuario y solicita la informacion necesaria
#AbstractBaseUser define datos de identidicacion de cada artista
#PermissionMixin ayuda a gestionar permisos especificos
#Group ayuda a organizar distintas categorias
#Permission ayuda a definir permisos especificos


class ArtistaManager(BaseUserManager):
    def create_artista(self, email, password, nombre, bio, imagen=None):
        if not email:
            raise ValueError('Por favor, ingrese un correo electrónico válido.')
        email = self.normalize_email(email)

        artista = self.model(
            email=email,
            nombre=nombre,
            bio=bio,
            imagen=imagen,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        artista.set_password(password)
        artista.save(using=self._db)
        return artista

class Artista(AbstractBaseUser, PermissionsMixin):
    rut          = models.CharField(max_length=13, primary_key=True)
    alias        = models.CharField(max_length=25, blank=True, null=True)
    first_name   = models.CharField(max_length=25, blank=False, null=True)
    last_name    = models.CharField(max_length=25, blank=False, null=True)
    ap_materno   = models.CharField(max_length=25, blank=False, null=True)
    fecha_nac    = models.DateField(blank=False, null=True)
    telefono     = models.IntegerField(blank=False, null=True)
    region       = models.CharField(max_length=20, blank=False, null=True)
    ciudad       = models.CharField(max_length=20, blank=False, null=True)
    comuna       = models.CharField(max_length=20, blank=False, null=True)
    direccion    = models.CharField(max_length=100, blank=False, null=True)
    email        = models.EmailField(max_length=40, blank=False, null=False, unique=True)
    password     = models.CharField(max_length=15, blank=False, null=False)

    bio          = models.TextField()
    imagen       = models.ImageField(upload_to='galeria_art', blank=True, null=True)
    is_active    = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)

    groups       = models.ManyToManyField(Group, related_name='artistas')
    user_permissions = models.ManyToManyField(Permission, related_name='artistas')

    objects = ArtistaManager()

    USERNAME_FIELD = 'email'                #Campos que se utilizan como identificacion del artista
    REQUIRED_FIELDS = ['rut']

    def __str__(self):
        return f"{self.rut} - {self.alias or 'Sin Alias'} - {self.first_name} {self.last_name} {self.ap_materno}"

