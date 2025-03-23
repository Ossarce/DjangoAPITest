from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  UserApp.views import UserViewSet, CategoryViewSet, ProductViewSet, SalesHistoryViewSet

router = DefaultRouter()

 #Se agregan basename para mayor claridad, pero definiendo queryset pareciera no ser necesario este argumento
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'sales', SalesHistoryViewSet, basename='sales')

urlpatterns = [
    path('', include(router.urls)),
]