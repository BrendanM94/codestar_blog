from django.contrib import admin
from django.urls import path
from blog.views import my_blog  # <-- ADD THIS IMPORT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', my_blog, name='blog'),  # <-- ADD THIS LINE
]
