from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

@csrf_exempt
def index(request):
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')   
    
    if request.method == 'GET':
        date = request.GET.get('date')
        word = request.GET.get('word')
        
        if word and date:
            tasks = tasks.filter(created_at=date, title__contains=word)
            
        if date:
            tasks = tasks.filter(created_at=date)
        
        if word:
            tasks = tasks.filter(title__contains=word)
        
    context = {'tasks': tasks} 
    return render(request, 'index.html', context)

@csrf_exempt
def delete(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')

@csrf_exempt
def update_status(request, id):
    task_status = (Task.objects.filter(id=id))[0].completed
    task = Task.objects.filter(id=id)
    if task_status == True:
        task.update(completed=False)
    else:
        task.update(completed=True)
    return redirect('/')