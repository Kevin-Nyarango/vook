from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.TextField()
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)


class TechStack(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = (models.SlugField(max_length=200, db_index=True))
    work_scope = models.CharField(max_length=100)
    tech_stacks = models.ManyToManyField(TechStack, blank=True)
    website = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
