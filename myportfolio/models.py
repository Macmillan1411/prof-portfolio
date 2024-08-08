from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='uploads/images', height_field=None, width_field=None)
    descrption = models.TextField()

    def __str__(self):
        return self.title

    
