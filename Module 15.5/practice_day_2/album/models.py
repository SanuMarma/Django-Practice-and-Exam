from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50)

    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    release_date = models.DateField()

    ratings = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]
    rating = models.CharField(max_length=50, choices=ratings)
    
    def __str__(self):
        return f'ID: {self.id} - {self.album_name}'
