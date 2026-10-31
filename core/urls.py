
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]
