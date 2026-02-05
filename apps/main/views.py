from django.shortcuts import render, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, 'main/task_list.html', {'task': tasks,})
@login_required()
def task_edit(requst, id):
    task = get_object_or_404(Task, id=id)
    return render(requst, 'main/task_edit.html', {'task': task,})