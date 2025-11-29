from django.urls import path

from todo.views import HomePageView, TagPageListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', TagPageListView.as_view(), name='tag'),
]