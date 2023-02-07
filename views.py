from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'tasks/home.html', {
        'new_task_name': request.POST.get('task_name', ''),
    })
