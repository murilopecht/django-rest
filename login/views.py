from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


def cad_user(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'registration/register.html', {'form_usuario': form_usuario})

@login_required
def show_users(request):
    
    all_users= User.objects.all()
    
    context= {'allusers': all_users}
        
    return render(request, 'registration/list.html', context)