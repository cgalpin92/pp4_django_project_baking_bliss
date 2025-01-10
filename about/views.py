from django.shortcuts import render
from .models import About

# Create your views here.

def about_baking_bliss(request):

    about = About.objects.all()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
