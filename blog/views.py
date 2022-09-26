from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.
def home(request):
    all_posts = Post.newmanager.all()
    return render(request,'blog/home.html',{'allposts':all_posts})


def post_single(request,post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request,'blog/single.html',{'post':post})

def search(request):
    return render(request,'blog/search.html')

