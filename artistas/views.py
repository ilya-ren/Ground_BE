from django.shortcuts import render, redirect
from .models import Artista
from django.contrib.auth.decorators import login_required
from .forms import ArtistaForm
from django.contrib.auth.hashers import make_password

# Create your views here.



def crud_artistas(request):
    artistas = Artista.objects.all()
    context = {'artista':artistas}
    print("enviando datos...")
    return render(request, "artistas/artistas_list.html", context)

def artistas_add(request):
    context={}

    if request.method == "POST":
        rut=request.POST["rut"]
        password=request.POST["password"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        fecha_nac=request.POST["fec_nac"]
        telefono =request.POST["tel"]
        region=request.POST["region"]
        ciudad=request.POST["ciudad"]
        comuna=request.POST["comuna"]
        direccion=request.POST["dire"]

        artista_manager= Artista.objects

        artista = artista_manager.create_user(rut=rut,password=password, email=email, first_name=first_name, last_name=last_name,fec_nac=fecha_nac, tel=telefono, region=region, ciudad=ciudad, comuna=comuna, dire=direccion)

        return redirect('artistas_add')
    else:
        context= {}
        return render(request, 'artistas/artistas_add.html', context)
  
def artistas_edit(request, pk):
    artista = Artista.objects.get(rut=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            if 'password' in form.changed_data:
                form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            print("Dato guardado exitosamente.")
            return redirect('artistas_edit', pk=pk)
        else:
            print("El formulario no es válido")
            print(form.errors)
    else:
        form = ArtistaForm(instance=artista)
    context = {'artista': artista, 'form': form}
    return render(request, 'artistas/artistas_edit.html', context)
    
def artistas_del(request, pk):
    mensajes=[]
    errores=[]
    artistas = Artista.objects.all()
    try:
        artistas= Artista.objects.get(rut=pk)
        context={}
        if artistas:
            artistas.delete()
            mensajes.append("Listo: Datos eliminados")
            context = {'artista':artistas, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'artistas/artistas_list.html', context)
        else:
            context={}
            return render(request, 'artistas/artistas_list.html', context)
    except:
        print("El artista indicado, NO existe.")
        artistas=Artista.objects.all()
        mensaje="El artista indicado, NO existe."
        context={'mensaje':mensaje, 'artistas':artistas}
        return render (request, 'artistas/artistas_list.html', context)
