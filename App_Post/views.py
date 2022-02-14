from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Authentication
from django.contrib.auth.decorators import login_required
# FORMS
from App_Post.forms import PostForm
# Models
from App_Post.models import Post
from django.contrib.auth.models import User
from App_Login.models import Follow
from App_Post.models import Like
# Create your views here.
@login_required
def Home(request):
    # This part of all Post Display process
    following_list = Follow.objects.filter(follower=request.user)
    Posts = Post.objects.filter(author__in=following_list.values_list('following'))
    # End of  all post  Display process
    # This part of all post like process
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    # End of all post like process
    # This part of search button process
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__contains=search)
    # End of search button process
    diction = {'search': search, 'result': result, 'Posts': Posts, 'like_post_list': liked_post_list}
    return render(request, 'App_Post/home.html', context=diction)

@login_required
def user_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post. author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    diction = {'form': form}
    return render(request, 'App_Post/post_form.html', context=diction)

@login_required
def Like_user(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    if not already_liked:
        liked = Like(post=post, user=user)
        liked.save()
    return HttpResponseRedirect(reverse('App_Post:home'))

@login_required
def Unlike_user(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Post:home'))
