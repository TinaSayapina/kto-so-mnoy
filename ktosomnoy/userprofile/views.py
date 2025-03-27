from django.shortcuts import render
from .models import UserProfile
from pprint import pprint
from .forms import ProfileForm


# Create your views here.

def profile_view(request):
     profile = UserProfile.objects.get(user_id=request.user.id)
     return render(request, 'profile.html',context={'profile':profile})

def profile_form(request):
    form = ProfileForm(request.POST)
    profile = UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'GET':
        return render(request,'profile_form.html')
    if request.method == 'POST':
        if form.is_valid():
            city = form.cleaned_data.get('city')
            district = form.cleaned_data.get('district')

            profile.city = city
            profile.district = district
            profile.save(update_fields=['city','district'])
        return render(request, 'profile.html',context={'profile':profile})

