from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Categories, Users, Tasks
from .forms import CreateTaskForm

# Create your views here.

def task_categories(request):
    category = Categories.objects.all()
    return render(request, 'Task/home.html', {'category':category})

def create_task(request):
    if request.method == 'POST':
        forms = CreateTaskForm(request.POST)
        if forms.is_valid():
            # list_forms = forms.cleaned_data
            # title = list_forms['title']
            # start_date = list_forms['start_date']
            # start_time = list_forms['start_time']
            # end_date = list_forms['end_date']
            # end_time = list_forms['end_time']
            # user = list_forms['user']
            # completed = list_forms['completed']
            # category = list_forms['category']
            forms.save()
            # save_task = Tasks.objects.create(title=title, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, user=user, completed=completed, category=category)
            # messages.success(request, 'Task added successfully!', 'success')
            return redirect('task:task_categories')
    else:
        forms = CreateTaskForm()
    return render(request, 'Task/create_task.html', {'forms': forms})

def category_detail(request, category_id):
    # tasks = Tasks.objects.all()
    tasks = Tasks.objects.filter(category__id=category_id)
    return render(request, 'Task/category_detail.html', {'tasks':tasks})

def show_tasks(request):
    tasks = Tasks.objects.values()
    return render(request, 'Task/tasks.html', {'tasks':tasks})

def search_result(request):
    text = request.GET.get()
    result = Tasks.objects.filter(title__icontains = text)
    return render(request, 'Task/search_result.html', {'result':result})