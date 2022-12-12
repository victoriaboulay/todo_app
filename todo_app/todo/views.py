from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def index(request):
    all_todos = TodoItem.objects.all()
    return render(request, 'index.html', {
        'all_todos': all_todos,
    })

# def addTodo(request):
#     new_todo = TodoItem(task_name=request.POST['task_name'])
#     new_todo.save()
#     return HttpResponseRedirect('/')

def addTodo(request):
    if request.method == 'GET':
        # current_todo = TodoItem.objects.get(id=todo_id)
        return render(request, 'add.html')

    if request.method == 'POST':
        new_todo = TodoItem(task_name=request.POST['task_name'])
        new_todo.save()
        return HttpResponseRedirect('/')  

def deleteTodo(request, todo_id):
        current_todo = TodoItem.objects.get(id=todo_id)
        current_todo.delete()
        return HttpResponseRedirect('/')

def completeTodo(request, todo_id):
    current_todo = TodoItem.objects.get(id=todo_id)
    current_todo.completed = True
    current_todo.save()
    return HttpResponseRedirect('/')

def updateTodo(request, todo_id):
    if request.method == 'GET':
        current_todo = TodoItem.objects.get(id=todo_id)
        return render(request, 'update.html', {
            'current_todo': current_todo,
        })

    if request.method == 'POST':
        current_todo = TodoItem.objects.get(id=todo_id)
        current_todo.task_name = request.POST['task_name']
        if 'completed' in request.POST:
            current_todo.completed = True

        else:
            current_todo.completed = False
        current_todo.save()
        return HttpResponseRedirect('/')