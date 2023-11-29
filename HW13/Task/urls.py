from django.urls import path, include
from .views import task_categories, category_detail, show_tasks, edit_task, search, task_detail, delete_task, edit_task

urlpatterns = [
    path('', show_tasks, name='home'),
    path('category/', task_categories, name='task_categories'),
    path('createtask/', edit_task, name='create_task'),
    path('category/detail/<int:category_id>/', category_detail, name='detail_category'),
    path('task/detail/<int:task_id>/', task_detail, name='detail_task'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('search/', search, name='search'),
]