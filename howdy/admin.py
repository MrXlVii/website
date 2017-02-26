from django.contrib import admin
from django.db import models
from django.forms import *
from .models import Language, Project, ProjectInstance, Blog, Category
from tinymce.widgets import TinyMCE

# Register your models here.

class BlogForm(forms.ModelForm):
    some_field = forms.TextField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Blog

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20},)},
    }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectInstance)
admin.site.register(Blog)
admin.site.register(Category)
