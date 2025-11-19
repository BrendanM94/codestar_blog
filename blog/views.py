from django.views import generic

from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6
