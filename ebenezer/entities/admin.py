from django.contrib import admin


from django.db import models

from .models.person import Person

admin.site.register(Person)
