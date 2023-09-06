from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet,get_profile

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('profile/',get_profile ),
]
