from django.contrib import admin
from .models import Categories, Tasks
# Register your models here.


admin.site.register(Tasks)
admin.site.register(Categories)