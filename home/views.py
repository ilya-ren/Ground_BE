
from django.shortcuts import render, redirect

def login_principal(request):
    return render(request, 'home/login_principal.html')


def redirigir_login(request):
    tipo_usuario = request.POST.get('tipo_usuario')

    if tipo_usuario == 'artista':
        return redirect('iniciar_sesion_artista')
    elif tipo_usuario == 'cliente':
        return redirect('iniciar_sesion_cliente')
    else:
        # Manejar caso de tipo de usuario no válido
        return render(request, 'home/login_principal.html', {'ERROR': 'Tipo de usuario no válido'})
