from django.http import HttpResponse
from django.views.generic import ListView

from .models import Post


def my_blog(request):
    return HttpResponse("Hello, blog!")


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10
