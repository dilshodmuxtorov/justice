from django.urls import path
from .views import AccountsView,AccountsDetailView

urlpatterns = [
    path('api/allusers/', AccountsView.as_view()),
    path('api/allusers/<pk>/',AccountsDetailView.as_view())
]