from django.shortcuts import redirect
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods
from pages.forms import OrderForm

from .models import Order


@require_http_methods(["POST"])
def create_order(request: HttpRequest):
    name = request.POST["name"]
    phone = request.POST["phone"]
    message = request.POST["message"] or None
    if name and phone:
        Order.objects.create(name=name, phone=phone, message=message)

        return redirect(
            "/?msg=true"
        )
