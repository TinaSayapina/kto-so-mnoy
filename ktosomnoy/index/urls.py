from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('register', views.Register.as_view()),
    path('logout',views.logout_view),
    path('activity/<int:pk>', views.activity_page),
]