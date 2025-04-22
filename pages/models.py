# models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='cities/')
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True, help_text="خط العرض")
    longitude = models.FloatField(null=True, blank=True, help_text="خط الطول")

    def __str__(self):
        return self.name
class CityImage(models.Model):
    city = models.ForeignKey(City, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cities/gallery/')    


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


