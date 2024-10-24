from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name = 'food'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
]
