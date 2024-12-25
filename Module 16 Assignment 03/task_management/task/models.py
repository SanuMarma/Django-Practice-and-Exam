from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length=50)
    task_description = models.TextField()
    task_assign_date = models.DateField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_title} - {self.is_completed}"