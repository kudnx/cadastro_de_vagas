from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VagaViewSet

router = DefaultRouter()
router.register(r'vagas', VagaViewSet, basename='vagas')

urlpatterns = [
    path('', include(router.urls)),
]