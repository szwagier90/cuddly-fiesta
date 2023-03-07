from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home_page, name='home'),
    path(r'first_task_list_url', views.task_list, name='task_list'),
]
