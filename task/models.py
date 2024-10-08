from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    CHOICES = [
        ("Urgent", "Терміново"),
        ("High", "Високий"),
        ("Medium", "Середній"),
        ("Low", "Низький"),
        ("Not Urgent", "Не терміново"),
    ]
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=15,
        choices=CHOICES,
        default="Urgent"
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Worker)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.priority})"
