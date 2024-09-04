from django import forms
from .models import Post
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','text','category','tags','author','feature_image','thumbnail_image']

class UserSignUpForm(forms.ModelForm):
    username = forms.CharField(
        required=False,  # Make the username field optional
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
       
    )
        
    class Meta:
        model = User
        fields = ('username', 'password','phone_number','email','city','state','country','user_profile_image')

class userloginForm(forms.ModelForm):
    username = forms.CharField(
    required=False,  # Make the username field optional
    widget=forms.TextInput(attrs={'placeholder': 'Username'}),)
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'city',
            'state',
            'country',
        ) 
        exclude = ('password',)

# class CommentForm(forms.ModelForm):
#     class meta:
#         model = Comment
#         fields = (
#             'name',
#             'email',
#             'text',
#             'parent',
#         )


