from django.contrib import admin
from .models import City,CityImage,ContactMessage,CapturedCookie

admin.site.register(City)
admin.site.register(CityImage)

admin.site.register(ContactMessage)
admin.site.register(CapturedCookie)
