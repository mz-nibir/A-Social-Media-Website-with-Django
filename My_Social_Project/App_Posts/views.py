from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

from App_Login.models import UserProfile, Follow
from django.contrib.auth.models import User
from App_Posts.models import Post

# Create your views here.

@login_required
def home(request):
    # user jader follow korse tader list ti nibo..
    following_list = Follow.objects.filter(follower=request.user)
    # jade k follow korsi tader post gula ashbe
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    if request.method == 'GET':
        # je keyword ti likhe search kora hobe ta collect korbo..(name=search)
        search = request.GET.get('search', '')
        # __icontains--> pertially match holeo colbe..and case insensitive jodi contains ar age i dei
        result = User.objects.filter(username__icontains=search)

    return render(request, 'App_Posts/home.html', context={'title':'Home', 'search':search, 'result':result, 'posts':posts})
