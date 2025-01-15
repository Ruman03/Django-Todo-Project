from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'  # Make sure this points to the correct template
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('todo:index')

def register(request):
    if request.user.is_authenticated:
        return redirect('todo:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('todo:index')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('todo:login')
        
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date if due_date else None
        )
        return redirect('index')

    filter_type = request.GET.get('filter', 'all')
    tasks = Task.objects.filter(user=request.user)
    
    if filter_type == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_type == 'pending':
        tasks = tasks.filter(completed=False)
    
    return render(request, 'todo/index.html', {'tasks': tasks, 'filter_type': filter_type})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('todo:index')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('todo:index')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        task.due_date = due_date if due_date else None
        task.save()
        return redirect('todo:index')
    context = {
        'task': task,
    }
    return render(request, 'todo/edit_task.html', context)