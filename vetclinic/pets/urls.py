from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/<int:pk>/', views.owner_detail, name='owner_detail'),
    path('owners/new/', views.owner_create, name='owner_create'),
    path('owners/<int:pk>/edit/', views.owner_update, name='owner_update'),
    
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pets/new/', views.pet_create, name='pet_create'),
    path('pets/<int:pk>/edit/', views.pet_update, name='pet_update'),
    
    path('consultations/<int:pk>/', views.consultation_detail, name='consultation_detail'),
    path('consultations/new/', views.consultation_create, name='consultation_create'),
    path('consultations/<int:pk>/edit/', views.consultation_update, name='consultation_update'),
]
