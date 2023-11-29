from django.db import models
from django.utils import timezone
import jdatetime
from django.contrib.auth import get_user_model
# Create your models here.

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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="task")
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="task_category")

    def __str__(self):
        return self.title
    
    