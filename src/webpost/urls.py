from django.conf.urls import url, include
from rest_framework import routers
from views import PostViewSet

router = routers.DefaultRouter()
# Routers provide an easy way of automatically determining the URL conf.
router.register(r'posts', PostViewSet)

