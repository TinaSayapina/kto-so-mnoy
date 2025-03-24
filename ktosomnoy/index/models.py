from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(default='')
    image = models.ImageField(upload_to='static/img',default='')

    def __str__(self):
        return self.title