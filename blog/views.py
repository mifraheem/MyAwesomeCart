from django.shortcuts import render
from .models import Blogpost


# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    params = {'posts': myposts}
    return render(request, 'blog/index.html', params)


def blogpost(request, myid):
    post = Blogpost.objects.filter(post_id=myid)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
