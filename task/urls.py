from django.urls import path

from task.views import index, PositionsListView, PositionsDetailView, PositionsCreateView

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionsListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionsDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionsCreateView.as_view(), name="position-create"),
]

app_name = "task"
