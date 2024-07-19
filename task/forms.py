from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")