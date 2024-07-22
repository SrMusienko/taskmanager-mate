from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from task.models import Worker, Position, TaskType, Task


class AuthTestCase(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin",
        )
        self.client.force_login(self.admin_user)


class WorkerListViewTest(AuthTestCase):
    def setUp(self):
        super().setUp()
        self.position = Position.objects.create(name="Manager")
        self.worker1 = Worker.objects.create(
            username="worker1",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            position=self.position
        )
        self.worker2 = Worker.objects.create(
            username="worker2",
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
            position=self.position
        )
        self.worker3 = Worker.objects.create(
            username="worker3",
            first_name="Jake",
            last_name="Smith",
            email="jake@example.com",
            position=self.position
        )

    def test_search_by_username(self):
        url = reverse("task:worker-list")
        response = self.client.get(url, {"data": "worker1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "worker1")
        self.assertNotContains(response, "worker2")
        self.assertNotContains(response, "worker3")

    def test_search_by_first_name(self):
        url = reverse("task:worker-list")
        response = self.client.get(url, {"data": "John"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "worker1")
        self.assertNotContains(response, "worker2")
        self.assertNotContains(response, "worker3")

    def test_empty_search(self):
        url = reverse("task:worker-list")
        response = self.client.get(url, {"data": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "worker1")
        self.assertContains(response, "worker2")
        # self.assertContains(response, "worker3")

    def test_no_results(self):
        url = reverse("task:worker-list")
        response = self.client.get(url, {"data": "Nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no workers in task manager")


# -------------------Task-------------

class TaskListViewTest(AuthTestCase):
    def setUp(self):
        super().setUp()
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.task1 = Task.objects.create(
            name="Fix login issue",
            description="Fix the login issue for all users",
            task_type=self.task_type,
            deadline="2024-08-01",
            is_completed=False
        )
        self.task2 = Task.objects.create(
            name="Update homepage",
            description="Redesign the homepage",
            task_type=self.task_type,
            deadline="2024-08-02",
            is_completed=False
        )
        self.task3 = Task.objects.create(
            name="Fix logout issue",
            description="Fix the logout issue for all users",
            task_type=self.task_type,
            deadline="2024-08-03",
            is_completed=False
        )

    def test_search_by_name(self):
        url = reverse("task:task-list")
        response = self.client.get(url, {"data": "Fix login issue"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix login issue")
        self.assertNotContains(response, "Update homepage")
        self.assertNotContains(response, "Fix logout issue")

    def test_search_by_description(self):
        url = reverse("task:task-list")
        response = self.client.get(url, {"data": "Redesign the homepage"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update homepage")
        self.assertNotContains(response, "Fix login issue")
        self.assertNotContains(response, "Fix logout issue")

    def test_empty_search(self):
        url = reverse("task:task-list")
        response = self.client.get(url, {"data": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix login issue")
        self.assertContains(response, "Update homepage")
        self.assertContains(response, "Fix logout issue")

    def test_no_results(self):
        url = reverse("task:task-list")
        response = self.client.get(url, {"data": "Nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no tasks in task manager")


# -------------------TaskType-------------

class TaskTypeListViewTest(AuthTestCase):
    def setUp(self):
        super().setUp()
        self.task_type1 = TaskType.objects.create(name="Bug Fix")
        self.task_type2 = TaskType.objects.create(name="Feature Development")
        self.task_type3 = TaskType.objects.create(name="Maintenance")

    def test_search_by_name(self):
        url = reverse("task:task-type-list")
        response = self.client.get(url, {"name": "Bug Fix"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bug Fix")
        self.assertNotContains(response, "Feature Development")
        self.assertNotContains(response, "Maintenance")

    def test_empty_search(self):
        url = reverse("task:task-type-list")
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bug Fix")
        self.assertContains(response, "Feature Development")
        self.assertContains(response, "Maintenance")

    def test_no_results(self):
        url = reverse("task:task-type-list")
        response = self.client.get(url, {"name": "Nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "There are no task types in task manager"
        )


# ------------Position---------------

class PositionListViewTest(AuthTestCase):
    def setUp(self):
        super().setUp()
        self.client.force_login(self.admin_user)

        self.position1 = Position.objects.create(name="Manager")
        self.position2 = Position.objects.create(name="Developer")
        self.position3 = Position.objects.create(name="Tester")

    def test_search_by_name(self):
        url = reverse("task:position-list")
        response = self.client.get(url, {"name": "Manager"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manager")
        self.assertNotContains(response, "Developer")
        self.assertNotContains(response, "Tester")

    def test_empty_search(self):
        url = reverse("task:position-list")
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manager")
        self.assertContains(response, "Developer")
        self.assertContains(response, "Tester")

    def test_no_results(self):
        url = reverse("task:position-list")
        response = self.client.get(url, {"name": "Nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no positions in task manager")
