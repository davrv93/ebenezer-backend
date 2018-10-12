from django.contrib import admin


from django.db import models

from .models.class_ import Class
from .models.clase import Clase
from .models.domain import Domain
from .models.dominio import Dominio
from .models.diagnostic_tag import DiagnosticTag
from .models.defining_characteristics import DefiningCharacteristic
from .models.intervention_type import InterventionType
from .models.level import Level
from .models.pattern import Pattern
from .models.related_factor import RelatedFactor
from .models.taxonomia import Taxonomia
from .models.taxonomy import Taxonomy
from .models.type_of_level import TypeOfLevel


# Create your models here.


# Register your models here.

# admin.site.register(Class)
# admin.site.register(Clase)
# admin.site.register(Domain)
# admin.site.register(Dominio)
admin.site.register(DefiningCharacteristic)
admin.site.register(DiagnosticTag)
admin.site.register(InterventionType)

admin.site.register(Level)
# admin.site.register(Taxonomia)
admin.site.register(Pattern)
admin.site.register(RelatedFactor)

admin.site.register(Taxonomy)
admin.site.register(TypeOfLevel)
