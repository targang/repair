from django.shortcuts import redirect
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail


from .models import Order


@require_http_methods(["POST"])
def create_order(request: HttpRequest):
    name = request.POST["name"]
    phone = request.POST["phone"]
    message = request.POST["message"] or None
    email = f"Имя: {name}\nТелефон: {phone}\n"
    if message:
        email += f'Сообщение: {message}'
    if name and phone:
        try:
            Order.objects.create(name=name, phone=phone, message=message)
            send_mail(
                subject="Новая заявка",
                message=email,
                from_email='email',
                recipient_list=[
                    "email",
                ],
                fail_silently=False,
            )
            return redirect("/?msg=true")
        except:
            return redirect("/")
