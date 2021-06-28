from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, Login, Logout
from django.urls import reverse, reverse_lazy

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            pass

    dict={'title':'sign up . Instragram','form':form, 'registered':registered}
    return render(request, 'App_Login/sign_up.html', context= dict)
