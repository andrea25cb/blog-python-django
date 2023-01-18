from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def fashionblog(request):
    return render(request, 'blog/fashionblog.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

from .forms import PostForm

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog/post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
