from django.urls import path

from todo.views import HomePageView, TaskToggleStatusView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, TagListView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task/<int:pk>/toggle/', TaskToggleStatusView.as_view(), name='task_toggle'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/create/', TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag_delete'),
]