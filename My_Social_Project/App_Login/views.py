from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            user_profile = UserProfile(user=user)
            return HttpResponseRedirect(reverse('App_Login:login'))

    dict={'title':'sign up . Instragram','form':form, 'registered':registered}
    return render(request, 'App_Login/sign_up.html', context= dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user = authenticate(username=username, password=password)
            # check user active/ase ki na ..?
            if user is not None:
                login(request, user)
                pass

    return render(request, 'App_Login/login.html', context={'title':'login', 'form':form})
