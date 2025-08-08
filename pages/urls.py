from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('xss-test/', views.xss_test, name='xss_test'),
    path('collect/', views.collect, name='collect'),
]
