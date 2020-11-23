from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index),
    path('api/meals/', views.mealsView.as_view()),
]
