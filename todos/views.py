from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import HttpResponse
from .models import Task
# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task=request.POST['task']
    Task.objects.create(task=task)#from model
    # return HttpResponse('form submitted')
    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    #if get request then just load task if post then update send to server
    if request.method=='POST':
        new_task=request.POST['task']#input type name is task 
        get_task.task=new_task #TASK FIELD
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task
        }
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
