from django.contrib import admin
from django.urls import path
from blog.views import my_blog, PostListView  # <-- ADD THIS IMPORT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='blog'),
]
