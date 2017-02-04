from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Language(models.Model):
    """
    Model representing the project language (e.g. Python, Java, etc.).
    """
    name = models.CharField(max_length=200, help_text="Enter the project language")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Project(models.Model):
    """
    Model representing a Project on my CV.
    """
    title = models.CharField(max_length=200) #title of the project on CV
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the project")
    version = models.CharField('Version',max_length= 8, help_text="(max) 12 Character version number e.g. 1.0.1 or in progress")    
    language = models.ManyToManyField(Language, help_text="Select the language for this project")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('project-detail', args=[str(self.id)])


class ProjectInstance(models.Model):
    """
    Model representing a specific instance of a project (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    late_update = models.DateField(null=True, blank=True)

    PROJECT_STATUS = (
        ('e', 'Early Phases'),
        ('a', 'Alpha'),
        ('b', 'Beta'),
        ('c', 'Completed/Released'),
    )

    status = models.CharField(max_length=1, choices=PROJECT_STATUS, blank=True, default='e', help_text='Project status')

    class Meta:
        ordering = ["last_update"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.project.title)
