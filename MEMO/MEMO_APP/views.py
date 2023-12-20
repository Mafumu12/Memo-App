from django.shortcuts import render, redirect
from .models import TASK
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import new_form
from django.db.models import Q

# Create your views here.

from django.db.models import Q

@login_required
def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the 'goals' parameter from the query string
        goals = request.GET.get('goals', '')

        # Filter tasks belonging to the current user
        tasks = TASK.objects.filter(owner=request.user)
        
        # Count incomplete tasks for display
        incomplete_tasks = tasks.filter(status=False).count()

        # Filter tasks based on 'goals' parameter using Q objects for flexible queries
        if goals:
            tasks = tasks.filter(Q(title__icontains=goals) | Q(description__icontains=goals))

        # Prepare context data to be passed to the template
        context = {'tasks': tasks, 'goals': goals, 'incomplete_tasks': incomplete_tasks}
        
        # Render the 'home.html' template with the context data
        return render(request, 'home.html', context)
    else:
        # If user is not authenticated, redirect to login page
        return redirect('REGISTRATION_APP:login')

@login_required
def new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Create a form instance and populate it with POST data
            form = new_form(request.POST)
            
            # Check if the form is valid
            if form.is_valid():
                # Save the new task to the database, linking it to the current user
                New_task = form.save(commit=False)
                New_task.owner = request.user
                New_task.save()
                
                # Redirect to the home page after successful task creation
                return redirect('MEMO_APP:home')
        else:
            # If the request method is GET, create an empty form instance
            form = new_form()
            
        # Prepare context data to be passed to the template
        context = {'form': form}
        
        # Render the 'new.html' template with the context data
        return render(request, 'new.html', context)
    else:
        # If user is not authenticated, redirect to login page
        return redirect('REGISTRATION_APP:login')

@login_required
def edit(request, id):
    # Get the task object to be edited
    tasks = TASK.objects.get(pk=id)
    
    # Check if the current user owns the task
    if request.user == tasks.owner:
        if request.method == 'POST':
            # Create a form instance and populate it with POST data and existing task data
            form = new_form(request.POST, instance=tasks)
            
            # Check if the form is valid
            if form.is_valid():
                # Save the edited task to the database
                form.save()
                
                # Redirect to the home page after successful task editing
                return redirect('MEMO_APP:home')
        else:
            # If the request method is GET, create a form instance populated with task data
            form = new_form(instance=tasks)
            
            # Prepare context data to be passed to the template
            context = {'form': form}
            
        # Render the 'edit.html' template with the context data
        return render(request, 'edit.html', context)
    
    # Render the 'edit.html' template (no context data) if user doesn't own the task
    return render(request, 'edit.html')

@login_required
def delete(request, id):
    # Get the task object to be deleted
    tasks = TASK.objects.get(pk=id)
    
    # Delete the task from the database
    tasks.delete()
    
    # Redirect to the home page after successful task deletion
    return redirect('MEMO_APP:home')

@login_required
def mark_task_completed(request, id):
    # Get the task object to be marked as completed or not
    task = TASK.objects.get(pk=id)
    
    # Toggle the status of the task (completed or not)
    task.status = not task.status
    
    # Save the updated task status to the database
    task.save()
    
    # Redirect to the home page after updating task status
    return redirect('MEMO_APP:home')
