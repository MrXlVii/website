from django.contrib import admin
from django import forms
from .models import Language, Project, ProjectInstance, Post, Category

# Register your models here.

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    form = PostForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectInstance)
admin.site.register(Post)
admin.site.register(Category)
