from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts_blog.forms import UserRegistrationForm


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("compte:login")
    else:
        form = UserRegistrationForm
    return render(request, "accounts_blog/signup.html", context={"form": form})


def profile(request):
    return redirect("compte:login")
