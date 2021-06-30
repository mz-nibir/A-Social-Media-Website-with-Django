from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile

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
            pass

    dict={'title':'sign up . Instragram','form':form, 'registered':registered}
    return render(request, 'App_Login/sign_up.html', context= dict)
