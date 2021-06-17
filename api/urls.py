from rest_framework import routers
from django.urls import path, include

from .views import TodoViewset, HomepageView

router = routers.SimpleRouter()
router.register(r'', TodoViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', HomepageView),
    path('todos/', include(router.urls)),
]
