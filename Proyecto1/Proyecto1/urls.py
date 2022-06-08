"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from MessageApp.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', acceso, name="acceso"),
    path('index/', index, name = "index"),
    path('register/', register, name = "register"),
    path('login/', login_request, name = "login"),
    path('logout/', LogoutView.as_view(template_name='acceso.html'), name='logout'),
    path('read_post/', read_post,  name = "read_post"),
    path('delete/<pk>', delete, name = "delete"),
    path('update_post/<pk>', update_post, name = "update_post"),
    path('create_post/', create_post, name = "create_post"),
    path('update_user/', update_user, name = "update_user"),
    path('login_copy/', login_correct, name = "login_correct"),
    path('profile/', profile, name = "profile"),
    path('read_more/<pk>', read_more, name = "read_more"), 
    path('create_message/', create_message, name = "create_message"), 
    path('post/', posteo, name = "posteo"),
    path('contacs/', buscar_usuario, name = "buscar_usuario"),
    path('about/', about, name = "about"),
    path('create_foro/', create_foro , name = "create_foro"), 
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)