from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.views import View
from django.shortcuts import render

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



def HomepageView(request):
    return render(request, 'index.html')