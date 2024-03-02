from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key = True)
    task = models.CharField(max_length = 255)
    completed = models.BooleanField(default = False)
    
    def __str__(self):
        return (f"{self.id} {self.task}")

# Create your models here.
