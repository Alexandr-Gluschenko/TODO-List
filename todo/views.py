from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Tag


# Create your views here.
class HomePageView(ListView):
    model = Task
    template_name = 'home/home_page.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.order_by('is_done', '-created_at')


class TagPageListView(ListView):
    model = Tag
    template_name = 'home/tag_page.html'