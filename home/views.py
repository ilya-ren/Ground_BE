
from django.shortcuts import render, redirect

def login_principal(request):
    context = {}
    return render(request, 'home/login_principal.html', context)


def redirigir_login(request):
    tipo_usuario = request.POST.get('tipo_usuario')

    if tipo_usuario == 'artista':
        return  redirect('login')
    elif tipo_usuario == 'cliente':
        return  redirect('login')
    else:
        # Manejar caso de tipo de usuario no válido
        return render(request, 'home/login_principal.html', {'ERROR': 'Tipo de usuario no válido'})
