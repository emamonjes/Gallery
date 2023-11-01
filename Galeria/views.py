from django.shortcuts import render
from .forms import UsuarioForm

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardar el usuario en la base de datos
            nuevo_usuario = form.save()
            # Realizar acciones adicionales si es necesario
    else:
        form = UsuarioForm()

    return render(request, 'Crear_Usuario.html', {'form': form})
