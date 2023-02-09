from django.shortcuts import redirect, render

from .models import Task

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Task.objects.create(name=request.POST['task_name'])
        return redirect('/tasks/')
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})
