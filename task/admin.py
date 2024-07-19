from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from task.models import Worker, Task, Position, TaskType
from task.forms import WorkerCreationForm, WorkerChangeForm


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    add_form = WorkerCreationForm
    form = WorkerChangeForm
    model = Worker
    search_fields = ("username", "first_name", "last_name")
    list_display = ("username", "first_name", "last_name", "email", "position", "is_staff", "is_active")
    list_filter = ("position", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "position")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "first_name", "last_name", "email", "position", "password1", "password2", "is_active", "is_staff"),
        }),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_filter = ("name", "deadline", "priority","assigned_to")


admin.site.register(Position)
admin.site.register(TaskType)

admin.site.unregister(Group)