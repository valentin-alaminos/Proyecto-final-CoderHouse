from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppCoder.models import *

# Create your views here.
def create_message(request):
    if request.method == 'POST':
        f_mensaje = MessageForm(request.POST)
        if f_mensaje.is_valid():
            texto =f_mensaje.cleaned_data
            NewMessage= message(message=texto['message'], emisor=texto['emisor'], receptor=texto['receptor'], date=texto['date'])
            NewMessage.save()

            messages = message.objects.all()

            contexto={'messages':messages}	
            return render(request, 'create_message.html', contexto)

    else:
        f_mensaje= MessageForm()
    return render(request, 'create_message.html', {'f_mensaje':f_mensaje})

def buscar_usuario(request):
    Contactos = User.objects.all()
    agenda = {'Contactos': Contactos}
    return render(request, 'contacs.html', agenda)



   
    
    
   
