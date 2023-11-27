from django.db import models
from django.utils import timezone
import jdatetime
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Categories(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    descrption = models.TextField()
    start_date = models.DateField(default=jdatetime.datetime.today().strftime('%Y-%m-%d'))
    start_time = models.TimeField(default=timezone.now)
    end_date = models.DateField(default=jdatetime.datetime.today().strftime('%Y-%m-%d'))
    end_time = models.TimeField(default=timezone.now)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="task")
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="task_category")

    def __str__(self):
        return self.title
    
    