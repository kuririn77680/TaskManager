from django.shortcuts import render
from app.models import Task

# Create your views here.
def index(request):
    obj = Task.objects.all().order_by('priority')
    return render(request, 'app/index.html', {'obj': obj})
