# your_app_name/urls.py
from django.urls import path
from . import views
from .views import xss_test
urlpatterns = [
    path('', views.home, name='home'),           # الصفحة الرئيسية
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('booking/', views.booking, name='booking'), # صفحة الحجز
    path("xss/", xss_test, name="xss-test"),
    path('contact/', views.contact, name='contact'), # صفحة التواصل
]
