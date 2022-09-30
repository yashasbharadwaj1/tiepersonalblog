from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Post,Category
from .forms import NewCommentForm,Postsearchform
from django.db.models import Q
# Create your views here.
def home(request):
    all_posts = Post.newmanager.all()
    return render(request,'blog/home.html',{'allposts':all_posts})


def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'blog/single.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form})

    

def search(request):
    form = Postsearchform()
    c = ''
    results = []
    query = Q()
    if "c" in request.GET:
        form = Postsearchform(request.GET)
        form.full_clean()
        if form.is_valid():
            c = form.cleaned_data['c']
            if c is not None:
                query &= Q(category=c)
        results = Post.objects.filter(query)
        print(results)

    return render(request,'blog/search.html',{'c':c,'form':form,'results':results})

