from django.shortcuts import render

# Create your views here.
from .models import user


def home(request):
    data = user.objects.all()
    context = {"data": data}

    return render(request, "grapp/index.html", context)
