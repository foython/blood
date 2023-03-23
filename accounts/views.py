from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from . form import UserCreationForm, UserChangeForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('index')
        else:
            messages.info(request, 'Username Password not matched')
            return redirect(request.path)

    return render(request, 'login.html')


def user_reg(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'regipage.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))