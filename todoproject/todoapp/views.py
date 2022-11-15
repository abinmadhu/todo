from django.shortcuts import render, redirect
from todoapp.forms import TaskForm
from .models import Task
from django.views.generic import ListView
# Create your views here.

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
        return redirect('/')
    else:
        task = Task()
        return render(request, 'index.html', {'task1': task1})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    else:
        return render(request, 'delete.html')

def update(request,task_id):
    if request.method=='POST':  
        task=Task.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        task=Task.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)       
        return render(request, 'update.html',{'form':form,'task':task})