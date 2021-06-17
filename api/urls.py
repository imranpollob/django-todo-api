from rest_framework import routers
from django.urls import path, include

from .views import TodoViewset

router = routers.SimpleRouter()
router.register(r'todos', TodoViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
