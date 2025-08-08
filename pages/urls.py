from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('xss/', views.xss_test, name='xss-test'),
    path('collect/', views.receive_cookie, name='receive-cookie'),
    path('view/', views.view_cookies, name='view-cookies'),
]
