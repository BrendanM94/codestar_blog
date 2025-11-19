from . import views
from django.urls import path

urlpatterns = [
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]
