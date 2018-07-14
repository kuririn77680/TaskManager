from django.shortcuts import render
from app.models import Task

# Create your views here.
def index(request):
    obj = Task.objects.all()
    return render(request, 'app/index.html', {'obj': obj})

def switch(request):
    # value add to parameters
    # new_priority add to parameters
    obj = Task.objects.get(action='prendre mon billet de train')
    Task.switch(obj, 1)
    obj = Task.objects.all()
    return render(request, 'app/index.html', {'obj': obj})
