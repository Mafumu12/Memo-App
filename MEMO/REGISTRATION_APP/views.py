from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Function for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('MEMO_APP:home')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        context = {'user': request.user}
        return render(request, 'login.html', context)

# Function for user logout
def user_logout(request):
    logout(request)  # Logout the user
    return render(request, 'login.html')  # Redirect to the login page

# Function for user signup
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('REGISTRATION_APP:login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)  # Render the signup page
