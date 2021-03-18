from django.shortcuts import render, redirect
from social_feed.models import *
from social_feed.forms import *

# Create your views here.
# def share_song(request, id):
#     """
#     """

def display_posts(request):
    """
    Displays all posts in the database. Will be updated to be based on the users
    the logged in user follows only.
    Last updated: 3/17/21 by Jacelynn Duranceau, Katie Lee, Marc Colin, Joe Frost
    """
    post_list = Post.objects.order_by('-date_created')
    #comment_list = Comment.objects.order_by('date_created')
    postform = PostForm()

    context = {
        'post_list': post_list,
        #'comment_list': comment_list,
        'postform': postform, 
        }  
    return render(request, 'social_feed/posts.html', context)

def create_post(request):
    """
    Creates a post. Redirects to the feed, which is where it will show up.
    Last updated: 3/17/21 by Jacelynn Duranceau, Katie Lee, Marc Colin, Joe Frost
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.text = form.cleaned_data.get('text')
            post.user_profile_fk = UserProfile.objects.get(pk=request.user.id)
            post.save()
    return redirect('/feed/')