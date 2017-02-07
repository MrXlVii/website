from django.contrib import admin
from .models import Language, Project, ProjectInstance

# Register your models here.

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectInstance)
