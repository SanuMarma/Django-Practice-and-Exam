from django.db import models
# from task.models import Task

# Create your models here.
class Category(models.Model):
    # id = models.AutoField(max_length=50)
    name = models.CharField(max_length=100)
    # task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name