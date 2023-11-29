from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Categories, Tasks
from .forms import EditTaskForm

# Create your views here.

def task_categories(request):
    category = Categories.objects.all()
    return render(request, 'Task/categories.html', {'category':category})

@login_required
def edit_task(request , task_id):
    # task = Tasks.objects.get(id=task_id)
    task = get_object_or_404(Tasks, pk=task_id)
    if task.user != request.user:
        raise Http404('شما امکان ویرایش این تسک را ندارید!')
    else:
        if request.method == 'POST':
            forms = EditTaskForm(request.POST, instance=task)
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
                return redirect('detail_task', task_id=task.id)
        else:
            forms = EditTaskForm(instance=task)
        return render(request, 'Task/edit_task.html', {'forms': forms})

def category_detail(request, category_id):
    # tasks = Tasks.objects.all()
    tasks = Tasks.objects.filter(category__id=category_id)
    return render(request, 'Task/category_detail.html', {'tasks':tasks})

def task_detail(request,task_id):
    # tasks = Tasks.objects.all()
    tasks = Tasks.objects.filter(id=task_id)
    return render(request, 'Task/task_detail.html', {'tasks':tasks})

def show_tasks(request):
    tasks = Tasks.objects.values()
    return render(request, 'Task/tasks.html', {'tasks':tasks})

def search(request):
    query = request.GET.get('query')
    results = Tasks.objects.filter(title__icontains=query)
    return render(request, 'Task/search.html', {"results":results})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    if task.user != request.user:
        raise Http404('شما امکان حذف این تسک را ندارید!')
    else:
        del_task = task.delete()
    return render(request, 'accounts/user_page.html')


