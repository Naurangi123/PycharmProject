from django.db import models

# Create your models here.
class Project(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=15)
    password2=models.CharField(max_length=15,null=True)


class Data(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=250)
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True,null=True)