from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),  #nuevo
    path("", BlogListView.as_view(), name="home"),
]