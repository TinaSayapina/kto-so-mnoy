from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view),
    path('profile-form',views.profile_form)
]