from django import forms
from .models import Post
from tinymce_4.fields import TinyMCEModelField


class PostForm(forms.ModelForm):
    body = TinyMCEModelField(' Foo Content ')
    #  body = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')

