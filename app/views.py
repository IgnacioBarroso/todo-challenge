from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
import json

# Create your views here.
@csrf_exempt
def index(request):
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

@csrf_exempt
def delete(request, id):
    Task.objects.filter(id=id).delete()
    return JsonResponse({'message': "Success"}, status=200)

@csrf_exempt
def update_status(request, id):
    jd = json.loads(request.body)
    Task.objects.filter(id=id).update(completed=jd['completed'])
    return JsonResponse({'message': "Success"}, status=200)