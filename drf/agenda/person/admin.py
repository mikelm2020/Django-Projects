from django.contrib import admin
from .models import Hobby, Meeting, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Meeting)

