from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Authentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Forms
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth.forms import AuthenticationForm

# Models
from django.contrib.auth.models import User
from App_Login.models import UserProfile, Follow

# Create your views here.
def Sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:Login_user'))
    diction = {'form': form}
    return render(request, 'App_Login/signup.html', context=diction)

def Login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Post:home'))
    diction = {'form': form}
    return render(request, 'App_Login/login.html', context=diction)

@login_required
def Logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:Login_user'))


@login_required
def Edit_Profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    diction = {'form': form}
    return render(request, 'App_Login/edit_profile.html', context=diction)
@login_required
def user_profile(request):
    return render(request, 'App_Login/user_profile.html', context={})

@login_required
def User_other(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_Login:user_profile'))
    diction = {'user_other': user_other, 'already_followed': already_followed}
    return render(request, 'App_Login/user_other.html', context=diction)

@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_Login:user_other', kwargs={'username':username}))

def Unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:user_other', kwargs={'username': username}))

