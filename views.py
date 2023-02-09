from django.shortcuts import render

from .models import Task

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_task_name = request.POST['task_name']
        Task.objects.create(name=new_task_name)
    else:
        new_task_name = ''

    return render(request, 'tasks/home.html', {
        'new_task_name': request.POST.get('task_name', ''),
    })
