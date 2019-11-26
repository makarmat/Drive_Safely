from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

def images_upload_path(instance, filename):
    return '{}'.format(filename)

    
class Photo(models.Model):
    image = models.ImageField(upload_to = images_upload_path, width_field='width', height_field='height')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    add_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class Advice(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photos')
    
    def __str__(self):
        return self.title   

    