from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request,"error try again")
    context = {
        'form':form,
        'title':'Register User'
    }
        
    return render(request, 'users/register.html', context=context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "users/login.html", context)

@login_required(login_url='login')
def logout_User(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('profile')
        else:
            messages.info(request, 'there is error check again')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/update_profile.html', {'uform': uform, 'pform': pform, 'title':'Profile'})

@login_required(login_url='login')
def profileView(request):
    user = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'user':user})