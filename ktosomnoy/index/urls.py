from django.urls import path
from . import views
from .views import home_page, Register, logout_view

urlpatterns = [
    path('', home_page),
    path('register', Register.as_view()),
    path('logout',logout_view)
]