from django.urls import path

from . import views
from .views import (
    HomeView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]

app_name = "todo"
