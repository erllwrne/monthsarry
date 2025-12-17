# love/views.py
from django.shortcuts import render, redirect
from .models import LoveCard, Letter

def login_view(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        if name == "Shairyll" and date == "2023-06-18":
            return redirect("home")
        else:
            message = "You're not my Girlfriend 🤬"
    return render(request, "login.html", {"message": message})

def home_view(request):
    cards = LoveCard.objects.all()
    return render(request, "home.html", {"cards": cards})

def letter_view(request, letter_id):
    letter = Letter.objects.get(id=letter_id)
    return render(request, "letter.html", {"letter": letter})
