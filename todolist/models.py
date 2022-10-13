from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    

    # def __str__(self):
    #     return self.title
    