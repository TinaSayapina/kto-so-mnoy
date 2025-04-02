from django.shortcuts import render,redirect
from django.contrib.auth import login,logout

from .forms import RegForm
from .models import Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegForm
from django.views import View
# Create your views here.

def home_page(request):
    activities = Activity.objects.all()
    context = {
        'activities':activities
    }
    return render(request,'home.html',context)



class Register(View):
    template = 'registration/signup.html'

    def get(self,request):
        return render(request,self.template,{'form':RegForm})

    def post(self,request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username = username,
                                     email = email,
                                     password=password)
            user.save()

            login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'username or password not correct')
            return redirect('/register')

# Log out
def logout_view(request):
    logout(request)
    return redirect('/')

def activity_page(request,pk):
    activity = Activity.objects.get(id = pk)
    context = {
        'activity':activity
    }
    return render(request,'activity.html',context)