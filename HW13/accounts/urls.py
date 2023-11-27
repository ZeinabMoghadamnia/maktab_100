from django.urls import path, include
from .views import user_register, user_login, user_logout, User_page
# from .forms import CreateTaskForm

urlpatterns = [
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('user/<int:user_id>/', User_page, name='user_page_url'),
]