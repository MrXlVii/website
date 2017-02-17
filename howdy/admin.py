from django.contrib import admin
from .models import Language, Project, ProjectInstance, Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectInstance)
admin.site.register(Blog)
admin.site.register(Category)
