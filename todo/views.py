from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import redirect, get_object_or_404

from .forms import TaskForm, TagForm
from .models import Task, Tag


# Create your views here.
class HomePageView(ListView):
    model = Task
    template_name = 'home/home_page.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-created_at']

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('home')

class TagPageListView(ListView):
    model = Tag
    template_name = 'home/tag_page.html'


class TaskCreateView(CreateView):
    model = Task
    fields = ['content', 'deadline', 'tags']
    template_name = 'home/task_form.html'
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'home/task_update.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super(TaskUpdateView, self).get_initial()
        initial['created_at'] = self.object.created_at
        return initial


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'home/task_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'task'


class TagListView(ListView):
    model = Tag
    form_class = TagForm
    template_name = 'home/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'home/tag_create.html'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'home/tag_update.html'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'home/tag_delete.html'
    success_url = reverse_lazy('tag_list')
    context_object_name = 'tag'