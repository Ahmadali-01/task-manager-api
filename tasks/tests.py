from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Task


class TaskAPITests(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Initial task")
        self.list_url = reverse("task-list")
        self.detail_url = reverse("task-detail", args=[self.task.pk])

    def test_create(self):
        response = self.client.post(
            self.list_url, {"title": "New task"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(title="New task").exists())

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.task.pk)

    def test_put(self):
        response = self.client.put(
            self.detail_url,
            {
                "title": "Replacement task",
                "description": "Updated description",
                "status": "in_progress",
                "due_date": None,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Replacement task")

    def test_patch(self):
        response = self.client.patch(
            self.detail_url, {"status": "done"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "done")

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_short_title(self):
        response = self.client.post(
            self.list_url, {"title": "ab"}, format="json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.data["error"]["details"])

    def test_missing_title(self):
        response = self.client.post(self.list_url, {}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_status(self):
        response = self.client.patch(
            self.detail_url, {"status": "invalid"}, format="json"
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_date(self):
        response = self.client.patch(
            self.detail_url, {"due_date": "not-a-date"}, format="json"
        )
        self.assertEqual(response.status_code, 400)

    def test_not_found(self):
        response = self.client.get(
            reverse("task-detail", args=[999999])
        )
        self.assertEqual(response.status_code, 404)

    def test_malformed_json(self):
        response = self.client.post(
            self.list_url,
            data='{"title":',
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
