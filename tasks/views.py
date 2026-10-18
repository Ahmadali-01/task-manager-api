from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Create, list, retrieve, update, and delete tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = [
        "get", "post", "put", "patch",
        "delete", "head", "options",
    ]
