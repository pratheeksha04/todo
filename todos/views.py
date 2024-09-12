from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .models import Task
# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task=request.POST['task']
    Task.objects.create(task=task)#from model
    # return HttpResponse('form submitted')
    return redirect('home')