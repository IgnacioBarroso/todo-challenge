from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('index')
        else:
            data['form'] = form
            
    return render(request, 'registration/register.html', data)

@login_required
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

@login_required
def delete(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')

@login_required
def update_status(request, id):
    task_status = (Task.objects.filter(id=id))[0].completed
    task = Task.objects.filter(id=id)
    if task_status == True:
        task.update(completed=False)
    else:
        task.update(completed=True)
    return redirect('/')