from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Worker, Position, TaskType, Task


@login_required
def index(request):
    num_positions = Position.objects.all().count()
    num_task_type = TaskType.objects.all().count()
    num_tasks = Task.objects.all().count()
    workers = Worker.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_positions": num_positions,
        "num_task_type": num_task_type,
        "num_tasks": num_tasks,
        'workers': workers,
        "num_visits": num_visits + 1,
    }

    return render(request, "task/index.html", context=context)


class PositionsListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task/position_list.html"
    paginate_by = 5


class PositionsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    template_name = "task/position_form.html"
    success_url = reverse_lazy("task:position-list")


class PositionsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "task/position_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('worker_set')


class PositionsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task:position-list")
    template_name = 'task/position_confirm_delete.html'


class PositionsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task:position-list")
    template_name = "task/position_form.html"
