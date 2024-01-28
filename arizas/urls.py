from django.urls import path 
from .views import ArizaList,ArizaCreateView
urlpatterns = [
    path("api/arizalist/",ArizaList.as_view()),
    path("api/arizacreate/",ArizaCreateView.as_view())
]