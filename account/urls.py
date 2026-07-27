from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
from .views import RegisterAPIView,ProfileAPIView, LoginAPIView, LogoutAPIView, RefreshAPIView

urlpatterns=[
    path("register/",views.RegisterAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('refresh/',RefreshAPIView.as_view()),
    path('logout/',LogoutAPIView.as_view()),
    path('profile/',ProfileAPIView.as_view())
]