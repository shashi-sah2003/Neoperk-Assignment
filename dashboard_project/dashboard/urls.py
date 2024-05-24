from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('select/', views.select_country, name='select_country'),
    path('dashboard/', views.dashboard, name='dashboard'),
]