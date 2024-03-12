from django.urls import path, include
from .views import FoodViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', FoodViewset)


urlpatterns = [
    path('', include(router.urls)),
]