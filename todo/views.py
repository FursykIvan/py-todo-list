from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tag


class HomeView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    ordering = ["done", "-created"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:home")


class TaskStatusView(generic.View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.done = not task.done
        task.save()
        return redirect("todo:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo/tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo/tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo/tag_list")
