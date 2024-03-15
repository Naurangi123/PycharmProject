from django.db import models

# Create your models here.
class Project(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50 )
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=16)
    address = models.CharField(max_length=16)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    zip_code=models.CharField(max_length=25)
    country=models.CharField(max_length=25)

    # created_at = models.DateTimeField(auto_now_add=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=100)
    # phone = models.CharField(max_length=15)
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # zipcode = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


class Data(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=250)
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)