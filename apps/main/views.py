from django.shortcuts import render
from .models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.order_by('-id').first()
    return render(request, "index.html", {"settings": settings})
