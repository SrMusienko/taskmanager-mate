from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task.models import Position, Task, TaskType


class AdminPanelTest(TestCase):

    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",  # Укажите email
            password="admin",
        )
        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(
            name="Test position",
        )
        self.task_type = TaskType.objects.create(
            name="Test type",
        )
        self.worker = get_user_model().objects.create_user(
            username="Test",
            email="test@example.com",
            password="Test123",
            first_name="Test first",
            last_name="Test last",
            position=self.position
        )
        self.task = Task.objects.create(
            name="Test name",
            description="Test description",
            deadline=datetime.now() + timedelta(days=7),
            is_completed=False,
            priority="Urgent",
            task_type=self.task_type,
            created_at=datetime.now()
        )
        self.task.assigned_to.set([self.worker])

    def test_position_list_display(self) -> None:
        url = reverse("admin:task_position_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.position.name)

    def test_position_detail_display(self) -> None:
        url = reverse(
            "admin:task_position_change",
            args=[self.position.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.position.name,)

    def test_task_list_display(self) -> None:
        url = reverse("admin:task_task_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.task.name, )

    def test_worker_list_display(self) -> None:
        url = reverse(
            "admin:task_worker_changelist",
        )
        res = self.client.get(url)
        self.assertContains(res, self.worker.username, )
