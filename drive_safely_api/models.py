from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Advice(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title