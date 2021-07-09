from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from App_Posts.forms import PostForm

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
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))

    dict={'title':'sign up . Instragram','form':form, 'registered':registered}
    return render(request, 'App_Login/sign_up.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # check user active/ase ki na ..?
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home'))

    return render(request, 'App_Login/login.html', context={'title':'login', 'form':form})

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request, 'App_Login/profile.html', context={'form':form, 'title':'Edit Profile . Social'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # obj create korbo (post)..jekhane form er info save korbo but db te pathabo na..
            post = form.save(commit=False)
            # author ta set korbo...(je user use korse sei author hisebe set hobe)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/user.html', context={'title':'User', 'form':form})
