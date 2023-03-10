from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profiles', views.UserProfileView)
router.register('feed', views.ProfileFeedView)

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('', include(router.urls))
]
