from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("shop/cart/", views.cart, name="cart"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("you/left/the/system/", views.logged_out, name="logged_out"),
]
