from django.shortcuts import redirect, render

from .models import Task

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Task.objects.create(name=request.POST['task_name'])
        return redirect('/tasks/first_task_list_url')
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
