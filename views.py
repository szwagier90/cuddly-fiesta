from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    if request.method == "POST":
        return HttpResponse(request.POST['task_name'])
    return render(request, 'tasks/home.html')
