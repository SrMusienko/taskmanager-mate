from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from task.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position", "photo")


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position", "photo")


class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
