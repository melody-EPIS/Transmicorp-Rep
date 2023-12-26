
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def user_profile(request):
    return render(request, 'user-profile.html')

def settings(request):
    return render(request, 'settings.html')



def editar_perfil(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Manejar la edición del perfil
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('user_profile')  # Cambia 'user_profile' por el nombre correcto de la vista de perfil
    else:
        form = ProfileForm(instance=user_profile)

    # Manejar el cambio de contraseña
    password_form = CustomPasswordChangeForm(request.user)

    if request.method == 'POST' and 'change_password' in request.POST:
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión para evitar cerrar la sesión del usuario
            messages.success(request, 'Contraseña cambiada con éxito.')

    return render(request, 'editar_perfil.html', {'form': form, 'password_form': password_form})