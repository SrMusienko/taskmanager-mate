from django.urls import path

from task.views import (
    index,
    PositionsListView,
    PositionsDetailView,
    PositionsCreateView,
    PositionsDeleteView,
    PositionsUpdateView,
    TaskTypesListView,
    TaskTypesDetailView,
    TaskTypesDeleteView,
    TaskTypesUpdateView,
    TaskTypesCreateView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path("", index, name="index"),

    path("positions/", PositionsListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionsDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionsCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/delete/", PositionsDeleteView.as_view(), name="position-delete"),
    path("positions/<int:pk>/update/", PositionsUpdateView.as_view(), name="position-update"),

    path("task-type/", TaskTypesListView.as_view(), name="task-type-list"),
    path("task-type/<int:pk>/", TaskTypesDetailView.as_view(), name="task-type-detail"),
    path("task-type/create/", TaskTypesCreateView.as_view(), name="task-type-create"),
    path("task-type/<int:pk>/delete/", TaskTypesDeleteView.as_view(), name="task-type-delete"),
    path("task-type/<int:pk>/update/", TaskTypesUpdateView.as_view(), name="task-type-update"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

]

app_name = "task"
