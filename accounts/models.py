from django.db import models
# para cambiar el modo de ingrso a email clave
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# calse con operaciones para crae un usurio nuevo

class MyAccoutManager(BaseUserManager):
    def create_user(self, first_name, last_name,username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener email')

        if not username:
            raise  ValueError ('El usuario debe tener username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
#crar un super usaurio en la app

    def create_superuser(self, first_name, last_name,username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
# para metror por defecto para un super usuarios
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user




# capos que solitara el registro
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # campos atributios de django obligatorios

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # cambio a que el usurios sea el correo

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    #para que los emtodos se incluyan en el modelo,asi ya se utilizan las funciones
    object = MyAccoutManager()

    #listar los recor ques e liste un label

    def __str__(self):
        return self.email
    # sitiene permisos de administrador, solo si es admin tien permisos

    def has_perm(self, perm, obj=None):
        return self.is_admin
    # permiosos alos modulos

    def has_module_perms(self, add_label):
        return True      







