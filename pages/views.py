from django.shortcuts import render
from .models import GalleryImage, Service
from .forms import OrderForm


def index(request):
    gallery = GalleryImage.objects.all()
    services = Service.objects.all()
    form = OrderForm()
    return render(
        request,
        "index.html",
        {
            "gallery": gallery,
            "services": services,
            "form": form,
        },
    )
