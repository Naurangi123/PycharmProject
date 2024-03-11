from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from .models import Project,Data



# Create your views here.

def index(request):
    projects=Data.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'index.html', context)

def detail(request,pk):
    projects=Data.objects.get(pk=pk)
    context={
        'projects':projects
    }
    return render(request,'detail.html',context)

@requires_csrf_token
def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if Project.objects.filter(first_name=first_name).exists():
                messages.info(request, 'First Name Taken')
                return redirect('signup')
            elif Project.objects.filter(last_name=last_name).exists():
                messages.info(request, 'Last Name Taken')
                return redirect('signup')
            elif Project.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif Project.objects.filter(password=password).exists():
                messages.info(request, 'Password Taken')
                return redirect('signup')
            elif Project.objects.filter(password2=password2).exists():
                messages.info(request, 'Confirm Password Taken')
                return redirect('signup')
            else:
                # user = Project.objects.create_user(email=email, password=password)
                # user.save()

                # Log user in and redirect to settings page
                user_login = authenticate(email=email, password=password)
                login(request, user_login)

                # Create a Profile object for the new user
        #         new_profile = Project.objects.create(user=user, id_user=user.id)
        #         new_profile.save()
        #         return redirect('settings')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


@requires_csrf_token
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, email)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout_user(request):
    logout(request)
    return redirect('signin')
