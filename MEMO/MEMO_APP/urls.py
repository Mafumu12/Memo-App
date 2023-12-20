from django.contrib import admin
from django.urls import path
from .import views

# Set the app namespace for URL routing
app_name = 'MEMO_APP'

# Define the app's URL patterns
urlpatterns = [
    # Admin page URL
    path('admin/', admin.site.urls),

    # URL for the home view using the 'home' function from the 'views' module
    path('home/', views.home, name='home'),

    # URL for the new task creation view using the 'new' function from the 'views' module
    path('new/', views.new, name='new'),

    # URL for editing a task using the 'edit' function from the 'views' module
    # The '<str:id>' captures the task ID from the URL and passes it to the 'edit' function
    path('edit/<str:id>/', views.edit, name='edit'),

    # URL for deleting a task using the 'delete' function from the 'views' module
    # The '<str:id>' captures the task ID from the URL and passes it to the 'delete' function
    path('delete/<str:id>/', views.delete, name='delete'),

    # URL for marking a task as completed or not using the 'mark_task_completed' function
    # The '<str:id>' captures the task ID from the URL and passes it to the 'mark_task_completed' function
    path('complete/<str:id>/', views.mark_task_completed, name='complete'),
]
