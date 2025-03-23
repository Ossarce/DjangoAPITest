from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  UserApp.views import USerViewSet

router = DefaultRouter()

router.register(r'users', USerViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]