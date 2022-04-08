
from django.contrib.auth.forms import UserCreationForm
from django  import forms
from .models import User,ProductReview






class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter UserName'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ReviewAdd(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('product','review_text','review_rating')        