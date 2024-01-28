from django.urls import path
from .views import UserCreateView,LoginView
urlpatterns = [
    path("signup/",UserCreateView.as_view()),
    path('api/login/', LoginView.as_view()),
]