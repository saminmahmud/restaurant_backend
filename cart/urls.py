from django.urls import path, include
from .views import CartViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CartViewset)


urlpatterns = [
    path('', include(router.urls)),
]