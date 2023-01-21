from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm,CommentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

            return redirect('post_detail')
    else:
        form = CommentForm()

        return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def fashionblog(request):
    return render(request, 'blog/fashionblog.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# def AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'add_comment.html'
#     success_url = reverse_lazy('post_list')
#     #fields = '_all_'