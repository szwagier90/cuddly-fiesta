from django.shortcuts import render

from .models import Task

# Create your views here.
def home_page(request):
    task = Task()
    task.name = request.POST.get('task_name', '')
    task.save()

    return render(request, 'tasks/home.html', {
        'new_task_name': request.POST.get('task_name', ''),
    })
