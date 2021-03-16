from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def listartasks(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task': task,'form':form}
    return render(request, 'ListTasks.html', context)

def deletetask(request,id):
    task = get_object_or_404(Task,pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    return render(request,'DeleteTask.html',{'task':task})


def updatetask(request,id):
    task = get_object_or_404(Task,pk=id)
    form = TaskForm(request.POST or None,request.FILES or None, instance=task)
    if request.method == 'POST':
        form.save()
        return redirect('tasks')
    return render(request,'UpdateTask.html',{'form':form})


