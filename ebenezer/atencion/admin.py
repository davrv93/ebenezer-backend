from django.contrib import admin


from django.db import models

from .models.class_ import Class
from .models.clase import Clase
from .models.domain import Domain
from .models.dominio import Dominio
from .models.intervention_type import InterventionType
from .models.level import Level
from .models.taxonomia import Taxonomia
from .models.taxonomy import Taxonomy
from .models.type_of_level import TypeOfLevel


# Create your models here.


# Register your models here.

# admin.site.register(Class)
# admin.site.register(Clase)
# admin.site.register(Domain)
# admin.site.register(Dominio)
admin.site.register(InterventionType)

admin.site.register(Level)
# admin.site.register(Taxonomia)
admin.site.register(Taxonomy)
admin.site.register(TypeOfLevel)
