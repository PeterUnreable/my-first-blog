from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
#Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog1/post_list.html', {'posts': posts})
     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'blog/post_list.html', {'posts': posts})
#blog/templates/blog/post_list.html
# return render (request, 'blog1/post_list.html', {})


def post1_list(request):

              posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
              return render(request, 'blog/pst.html', {'posts': posts})
