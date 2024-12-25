from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('form_field/', views.FormField, name = "form_field"),
    path('model_field/', views.Model, name = "model_field"),
]