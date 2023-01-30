from rest_framework import routers

from apps.core.views import UserViewSet


app_name = 'core'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
