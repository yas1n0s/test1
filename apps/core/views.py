from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from core.models import SiteInfo   # импортируем модель

def index(request):
    # Получаем первую запись из SiteInfo (обычно она одна)
    site_info = SiteInfo.objects.first()

    return render(request, "index.html", {"site_info": site_info})
