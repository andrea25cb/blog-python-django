from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def fashionblog(request):
    return render(request, 'blog/fashionblog.html')

def contacto(request):
    return render(request, 'blog/contacto.html')