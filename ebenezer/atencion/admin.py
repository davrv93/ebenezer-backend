from django.contrib import admin


from django.db import models

from .models.dominio import Dominio
from .models.clase import Clase


admin.site.register(Clase)

admin.site.register(Dominio)
# Create your models here.


# Register your models here.
