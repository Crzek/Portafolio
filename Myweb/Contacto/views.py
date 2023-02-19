from django.shortcuts import render

# Create your views here.
context ={
    'nombre':"Erick Cruz",
    "home": "Home",
    "contacto": "Contact",
    "about": "About",
    "home2": "Home"

}

def home(request):
    
    return render(request, "base.html", context)

def contacto(request):
    return render(request, "contact.html",context)

def about(request):
    return render(request, "about.html", context)


def home2(request):
    return render(request, "base2.html", context)
