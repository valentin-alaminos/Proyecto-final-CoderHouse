from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserLoginForm(forms.Form):
    username = forms.CharField(label= 'Nombre de usuario')
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)   

class PostForm(forms.Form): 
    title = forms.CharField(label= 'Titulo', max_length=100)
    subtitle = forms.CharField(label= 'Subtitulo', max_length=100, required=False)
    content = forms.CharField(label= 'Contenido', widget=forms.Textarea)
    date = forms.DateField(label= 'Fecha', initial=date.today) 
    image = forms.ImageField(label= 'image', required=False) 


    
    
class update_userform(forms.Form):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}




