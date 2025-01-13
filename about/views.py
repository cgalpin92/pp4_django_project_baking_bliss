from django.shortcuts import render
from .models import About

# Create your views here.

def about_baking_bliss(request):
    """
    Renders the most recent information on the website purpose 
    and allows user collaboration requests
    Displays an individual instance of :model:`about.About`
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form: `about.CollaborateForm`.
    **Template**
    :template: `about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
        }
        
    )
