from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    posts = Post.published.all()  # Özel manager kullanarak sadece yayınlanan postları alın
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, id):
    post = get_object_or_404(
        Post, 
        id=id,
        status=Post.Status.PUBLISHED  # Sadece yayınlanan postları alın
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
