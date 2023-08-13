from django.contrib import admin

from .models import Instance, Annotation

admin.site.register(Instance)
admin.site.register(Annotation)