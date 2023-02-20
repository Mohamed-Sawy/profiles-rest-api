from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profiles', views.UserProfileView)
router.register('login', views.LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls))
]
