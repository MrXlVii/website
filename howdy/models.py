from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
import uuid
from django.db.models import permalink
from django.utils import timezone
from tinymce_4.fields import TinyMCEModelField


# Create your models here.

class Language(models.Model):
    """
    (e.g. Python, Java, etc.).
    """
    name = models.CharField(max_length=200,
                            help_text="Enter the project language"
                            )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Project(models.Model):
    # Updated Project model.
    title = models.CharField(max_length=200, unique=True)
    summary = models.TextField(max_length=1000,
                               help_text="Enter a brief" +
                               " description of the project."
                               )
    language = models.ManyToManyField(Language,
                                      help_text="Select the" + 
                                      " language for this project"
                                     )
    last_update = models.DateField(null=True, blank=True)
    category = models.ForeignKey('Category')

    class Meta:
        ordering = ["last_update"]

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])    


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, default=uuid.uuid1)
    posted = models.DateField(db_index=True, auto_now_add=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return '%s' % self.title

    def publish(self):
        self.posted_date = timezone.now()
        self.save()

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
