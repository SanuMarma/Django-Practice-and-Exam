from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, primary_key=True)
    
    instruments_name = [
    ('guitar', 'Guitar'),
    ('ukulele', 'Ukulele'),
    ('cajon', 'Cajon'),
    ('flute', 'Flute'),
    ('violin', 'Violin'),
    ('piano', 'Piano'),
]
    instrument_type = models.CharField(max_length=50, choices=instruments_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


