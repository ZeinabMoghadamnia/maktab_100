from django.urls import path, include
from .views import task_categories, category_detail, show_tasks, create_task, search_result
from .forms import CreateTaskForm

urlpatterns = [
    path('', show_tasks, name='home'),
    path('category/', task_categories, name='task_categories'),
    path('createtask/', create_task, name='create_task'),
    path('detail/<int:category_id>/', category_detail, name='detail_category'),
    path('search/', search_result, name='search_result'),
]