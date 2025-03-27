from django.shortcuts import render
from .models import UserProfile
from pprint import pprint


# Create your views here.

def profile_view(request):
     profile = UserProfile.objects.get(user_id=request.user.id)
     return render(request, 'profile.html',context={'profile':profile})

def profile_form(request):
    user = request.user.id
