from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.models import Product

# Create your views here.


def index(request):
    user = request.user
    if user.is_anonymous:
        user_name = "Guest!"
    else:
        user_name = user.get_full_name() or user.username
    context = {
        "user_name": user_name,
    }
    return render(request, "core/index.html", context)


@login_required
def cart(request):
    user = request.user
    if user.is_anonymous:
        user_name = "Guest"
    else:
        user_name = user.get_full_name() or user.username
    return render(request, "core/cart.html", {"user_name": user_name})


def logged_out(request):
    return render(request, "core/logout.html")
