from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm, WorkerForm, CustomUserCreationForm
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
    paginate_by = 3


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


# ------- Task type -----------

class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task/task_type_list.html"
    paginate_by = 3


class TaskTypesDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "task/task_type_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(task_type=self.object)
        return context


class TaskTypesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task:task-type-list")
    template_name = 'task/task_type_confirm_delete.html'


class TaskTypesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_form.html"


class TaskTypesCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "task/task_type_form.html"
    success_url = reverse_lazy("task:task-type-list")


# ------- Task -----------

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 3

    def get_queryset(self):  # template may contain non-optimal data
        return Task.objects.prefetch_related('assigned_to')


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy("task:task-list")


# ------- Worker-----------

class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task/worker_list.html"
    paginate_by = 3


class WorkersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = CustomUserCreationForm
    template_name = "task/worker_form.html"
    success_url = reverse_lazy("task:worker-list")


class WorkersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    template_name = "task/worker_form.html"
    success_url = reverse_lazy("task:worker-list")


class WorkersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = 'task/worker_confirm_delete.html'
    success_url = reverse_lazy("task:worker-list")
