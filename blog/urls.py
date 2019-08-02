from django.urls import path 

from .views import BlogPageView, DetailPageView

urlpatterns = [
    path('post/<int:pk> ', DetailPageView.as_view(), name='post'),
    path('', BlogPageView.as_view(), name='index'),
]