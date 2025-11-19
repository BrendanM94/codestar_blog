from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6


def post_detail(request, slug):
    """Function-based view to display a single published post by slug."""
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})
