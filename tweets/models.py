from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
