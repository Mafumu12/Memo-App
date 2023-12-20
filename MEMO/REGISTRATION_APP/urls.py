from django.contrib import admin
from django.urls import path
from .import views

app_name = 'REGISTRATION_APP'  # Namespace for URL routing

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', views.user_login, name='login'),  # URL for user login
    path('signup/', views.user_signup, name='signup'),  # URL for user signup
    path('logout/', views.user_logout, name='logout'),  # URL for user logout
]
