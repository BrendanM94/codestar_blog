from django.views import generic

from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
