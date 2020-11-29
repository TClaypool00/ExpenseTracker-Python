from django.shortcuts import redirect, render
from .forms import CreatePostForm
from api.posts import PostsApi, posts_url
from api.reply import reply_url
from api.api import Api
from django.contrib.auth.decorators import login_required

@login_required()
def community_index(request):
    search = request.GET.get('search')
    all_posts = Api.get_all(Api, posts_url, user_id=None, search=search, post_id=None)
    return render(request, 'community_index.html', {'posts' : all_posts, 'search' : search})

@login_required()
def create_post(request):
    user_id = request.user.userid
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            PostsApi.create_post(PostsApi, form.cleaned_data['post_title'], form.cleaned_data['post_body'], user_id)
            return redirect('/community/home')
    else:
        form = CreatePostForm
        return render(request, 'create_post.html', {'form' : form})
    
@login_required()
def post_details(request, id):
    post = PostsApi.post_by_id(PostsApi, id)
    replies = Api.get_all(Api, reply_url, user_id=None, search=None, post_id=id)
    return render(request, 'post_details.html', {'post' : post, 'replies' : replies})