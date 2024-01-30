from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from django.contrib.auth.hashers import make_password



def crud_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    print("enviando datos...")
    return render(request, "clientes/clientes_list.html", context)

def clientes_add(request):
    context={}

    if request.method == "POST":
        rut=request.POST["rut"]
        password=request.POST["password"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        fecha_nac=request.POST["fecha_nac"]
        telefono=request.POST["tel"]
        region=request.POST["region"]
        ciudad=request.POST["ciudad"]
        comuna=request.POST["comuna"]
        direccion=request.POST["dire"]

        cliente_manager= Cliente.objects

        cliente = cliente_manager.create_user(rut=rut,password=password, email=email, first_name=first_name, last_name=last_name,fec_nac=fecha_nac, tel=telefono, region=region, ciudad=ciudad, comuna=comuna, dire=direccion)

        return redirect('clientes_add')
    else:
        context= {}
        return render(request, 'clientes/clientes_add.html', context)
    

def clientes_edit(request, pk):
    cliente = Cliente.objects.get(rut=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            if 'password' in form.changed_data:
                form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            print("Datos del Cliente guardados exitosamente!")
            return redirect('clientes_edit', pk=pk)
        else:
            print("Error. Datos del cliente invalidos.")
            print(form.errors)
    else:
        form = ClienteForm(instance=cliente)
    context = {'cliente': cliente, 'form': form}
    return render(request, 'clientes/clientes_edit.html', context)

def clientes_del(request, pk):
    mensajes=[]
    errores=[]
    clientes = Cliente.objects.all()
    try:
        clientes = Cliente.objects.get(rut=pk)
        context={}
        if clientes:
            clientes.delete()
            mensajes.append("Hecho, los datos han sido eliminados")
            context = {'clientes':clientes, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'clientes/clientes_list.html', context)
        else:
            context={}
            return render(request, 'clientes/clientes_list.html', context)
    except:
        print("ERROR. No existe tal cliente")
        clientes=Cliente.objects.all()
        mensaje="ERROR. No existe tal cliente"
        context={'mensaje':mensaje, 'clientes':clientes}
        return render (request, 'clientes/clientes_list.html', context)