from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm


# Create your views here.
def login_pg(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate to check the user is in the database
        user = authenticate(username=name, password=password)
        if user is not None:
            # login to generate session to add this user and be authenticated
            login(request, user)

            # this is to handle middleware
            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            return redirect('home:home')
        
        messages.info(request, "User Name or password is incorrect ")

    return render(request,'main/login.html')

def signout(request):
    logout(request)
    return redirect('auth_app:login')

def signup(request):

    if request.user.is_authenticated:
        return redirect("home:home")
    
    signup_form = UserForm()
    if request.method == "POST":
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()

            message = f"User account created for username: {signup_form.cleaned_data.get("username")}" 
            messages.info(request, message)
            return redirect('auth_app:login')
    
    context = {'signup_form': signup_form}
    return render(request, 'main/signup.html', context)