from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

@login_required
def base(request):
    return render(request, "index.html")

def salir(request):
    logout(request)
    return redirect('/')

def crear_cuenta(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/accounts/login/')
        else:
            data['form'] = user_creation_form

    return render(request, 'crear_cuenta.html', data)
