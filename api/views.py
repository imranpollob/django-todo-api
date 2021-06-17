from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
