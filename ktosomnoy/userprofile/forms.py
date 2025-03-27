from django import forms

class ProfileForm(forms.Form):
    city = forms.CharField(max_length=32)
    district = forms.CharField(max_length=32)
    social = forms.URLInput()
    photo = forms.ImageField(upload_to='static/img', default='')
    about = forms.Textarea()

