from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ToDoList, Task
from .forms import ToDoListForm, TaskForm
from django.http import JsonResponse

# 🚀 To-Do List Views
class ToDoListView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'tasks/todolist.html', {'todolists': None})
        
        todolists = ToDoList.objects.filter(user=request.user)
        return render(request, 'tasks/todolist.html', {'todolists': todolists})

class ToDoListDetailView(View):
    def get(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        tasks = todolist.tasks.all()
        return render(request, 'tasks/todolist_detail.html', {'todolist': todolist, 'tasks': tasks})

class ToDoListCreateView(View):
    def get(self, request):
        form = ToDoListForm()
        return render(request, 'tasks/todolist_form.html', {'form': form})
    
    def post(self, request):
        form = ToDoListForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.user = request.user
            todolist.save()
            return redirect('todolist-list')
        return render(request, 'tasks/todolist_form.html', {'form': form})

class ToDoListUpdateView(View):
    def get(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        form = ToDoListForm(instance=todolist)
        tasks = Task.objects.filter(todo_list__pk=pk)
        return render(request, 'tasks/todolist_form.html', {'form': form})
    
    def post(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        form = ToDoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect('todolist-list')
        return render(request, 'tasks/todolist_form.html', {'form': form})

class ToDoListDeleteView(View):
    def post(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        todolist.delete()
        return redirect('todolist-list')


# 🚀 Task Views
class TaskListView(View):
    def get(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        tasks = Task.objects.filter(todo_list=todolist)
        return render(request, 'tasks/tasklist.html', {'todolist': todolist, 'tasks': tasks})

class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, todo_list__user=request.user)
        return render(request, 'tasks/task_detail.html', {'task': task})

class TaskCreateView(View):
    def get(self, request, pk):
        form = TaskForm()
        tasks = Task.objects.filter(todo_list__pk=pk)
        return render(request, 'tasks/task_form.html', {'form': form, 'tasks': tasks, 'pk': pk})
    
    def post(self, request, pk):
        todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.todo_list = todolist
            task.save()
            return JsonResponse({
                'name': task.title,
                'status': task.get_status_display(),  # Assuming you have choices for the status
            })
        return JsonResponse({'errors': form.errors}, status=400)

class TaskUpdateView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, todo_list__user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_form.html', {'form': form, 'pk': pk})
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, todo_list__user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list', pk=task.todo_list.pk)
        return render(request, 'tasks/task_form.html', {'form': form})

class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, todo_list__user=request.user)
        return render(request, 'todo/confirm_delete.html', {
            'object': task, 
            'object_type': 'Task'
        })
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, todo_list__user=request.user)
        task.delete()
        return redirect('task-list', pk=task.todo_list.pk)
