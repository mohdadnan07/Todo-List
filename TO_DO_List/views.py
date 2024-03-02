from django.shortcuts import *
from . models import Task
from django.http import *
from django.contrib import messages

def index(request):
    fm = Task.objects.all()
    return render(request, 'index.html', {'tasks': fm})

def abc(request):
    ak = Task.objects.all()
    return render(request, 'addtask.html', {'ak': ak})

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        data = Task.objects.create(task = task)
        data.save()
        messages.info(request,'To Do Task Added In Task Table')
        return redirect('add_task')
    else:
        return render(request, 'addtask.html')
    
def complete_task(request, id):
    task = Task.objects.get(id = id)
    task.completed = True
    task.save()
    return redirect('index')
    