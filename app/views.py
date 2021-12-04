from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.

def index(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, json_dumps_params={'indent': 2}, safe=False)

@csrf_exempt
def create(request):
    jd = json.loads(request.body)
    Task.objects.create(title=jd['title'], content=jd['content'])
    return JsonResponse({'message': "Success"}, status=201)

@csrf_exempt
def delete(request, id):
    Task.objects.filter(id=id).delete()
    return JsonResponse({'message': "Success"}, status=200)

@csrf_exempt
def update_status(request, id):
    jd = json.loads(request.body)
    Task.objects.filter(id=id).update(completed=jd['completed'])
    return JsonResponse({'message': "Success"}, status=200)