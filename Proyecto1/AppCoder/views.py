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
from django.contrib.auth.decorators import login_required







def login_correct(request):
    return render(request,'login_copy.html')

def ok_update(request):
    return render(request,'ok_update.html')

def acceso(request):
    return render(request, "acceso.html")

def posteo(request):
    
    return render(request, 'post.html')
    
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
            
        if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                        login(request, user)
                        posts = post.objects.all()
                        context = {'posts': posts}
                        return render(request, 'read_post.html', context)
                
        else: 
            return render(request, 'login.html', {'form': form, 'mensaje': 'Usuario o contraseña incorrectos'})
        

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def index(request):
    return render(request, 'index.html')

def register(request):
    
    if request.method == 'POST':
        formR = UserRegisterForm(request.POST)
        if formR.is_valid():
             username = formR.cleaned_data['username']
             formR.save()
             posts = post.objects.all()
             context = {'posts': posts}
             return render(request, 'login_copy.html', context)
             

    else:
        formR = UserRegisterForm()


    return render(request, "register.html", {"formR":formR})
@login_required
def read_post(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request, 'read_post.html', context)

def  delete(request, pk):
    Post = post.objects.get(pk=pk)
    Post.delete()
    posts = post.objects.all()

    context = {'posts': posts}
    return render(request, 'read_post.html', context)


def update_post(request, pk):
    Post = post.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = PostForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            Post.title = informacion['title']
            Post.subtitle = informacion['subtitle']
            Post.content = informacion['content']
            Post.date = informacion['date']
            
            Post.save()
        
            posts = post.objects.all()
            context = {'posts': posts}
            return render(request, 'read_post.html', context)
    
    else:
        formulario = PostForm(initial={'title': Post.title, 'subtitle': Post.subtitle, 'content': Post.content, 'date': Post.date, 'image': Post.image})
    return render(request, 'update_post.html', {'formulario': formulario, 'pk' : pk })



def create_post(request):
    if request.method == 'POST':
        formu = PostForm(request.POST, files=request.FILES) 
        if formu.is_valid():
            informacion = formu.cleaned_data
            Newpost = post(title=informacion['title'], subtitle=informacion['subtitle'], content=informacion['content'], date=informacion['date'], image=informacion['image'])
            Newpost.save()

            posts = post.objects.all()
            context = {'posts': posts}
            return render(request, 'read_post.html', context)
    
    else:
        formu = PostForm()
    return render(request, 'create_post.html', {'formu': formu})






def update_user(request):
    User = request.user
    
    if request.method == 'POST':
        UserForm = UserRegisterForm(request.POST)
        if UserForm.is_valid():
            informacion=UserForm.cleaned_data
            User.username = informacion['username']
            User.email = informacion['email']
            User.set_password(informacion ['password1']) 
            
            User.save()


            return render (request, 'profile.html')  #vuelve a la pagina principal


    else:
        UserForm = UserRegisterForm(instance=User)
    return render(request, 'update_user.html', {'UserForm':UserForm})


def profile(request):
    return render(request,'profile.html')

def read_user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'profile.html', context) 

def read_more(request, pk):
    Posteo = post.objects.get(pk=pk)
    PosteoContext = {'Posteo': Posteo}  
    return render(request, 'post.html', PosteoContext)

def about(request):
    return render(request,'about.html')


