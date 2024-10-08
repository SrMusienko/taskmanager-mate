from django.urls import path

from task.views import (
    PositionsCreateView,
    PositionsDeleteView,
    PositionsDetailView,
    PositionsListView,
    PositionsUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskTypesCreateView,
    TaskTypesDeleteView,
    TaskTypesDetailView,
    TaskTypesListView,
    TaskTypesUpdateView,
    TaskUpdateView,
    WorkersCreateView,
    WorkersDeleteView,
    WorkersListView,
    WorkersUpdateView,
    index,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionsListView.as_view(),
        name="position-list"
    ),
    path(
        "positions/<int:pk>/",
        PositionsDetailView.as_view(),
        name="position-detail"
    ),
    path(
        "positions/create/",
        PositionsCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionsDeleteView.as_view(),
        name="position-delete"
    ),
    path(
        "positions/<int:pk>/update/",
        PositionsUpdateView.as_view(),
        name="position-update"
    ),

    path(
        "task-type/",
        TaskTypesListView.as_view(),
        name="task-type-list"),
    path(
        "task-type/<int:pk>/",
        TaskTypesDetailView.as_view(),
        name="task-type-detail"
    ),
    path(
        "task-type/create/",
        TaskTypesCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "task-type/<int:pk>/delete/",
        TaskTypesDeleteView.as_view(),
        name="task-type-delete"
    ),
    path(
        "task-type/<int:pk>/update/",
        TaskTypesUpdateView.as_view(),
        name="task-type-update"
    ),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),

    path(
        "workers/",
        WorkersListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/create/",
        WorkersCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkersUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkersDeleteView.as_view(),
        name="worker-delete"
    ),
]

app_name = "task"
