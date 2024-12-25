from django.db import models

# Create your models here.

class ModelField(models.Model):
    roll = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(unique=True, max_length=255)
    
    file_field = models.FileField(upload_to='./first_app/upload/')
    image_field = models.ImageField(upload_to='first_app/upload', null=True)
    # json_profile = models.JSONField()
    # positive_integer_field = models.PositiveIntegerField(null=True)
    # slug_field = models.SlugField()
    url_field = models.URLField()
    date_field = models.DateField()

    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'



    
    