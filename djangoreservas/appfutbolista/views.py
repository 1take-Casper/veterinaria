from http import server
from django.shortcuts import render, redirect
from . import forms
from .models import Mascota,Dueño,ReservaHora
from .serializers import ReservaSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')
@login_required

def listadoMascotas(request):
    mascotas=Mascota.objects.all()
    data={'mascotas':mascotas}
    return render(request,'listado.html',data)
@login_required

def agregarMascota(request):
    form = forms.RegistroMascotaForm()
    if request.method == 'POST':
        form_post = forms.RegistroMascotaForm(request.POST)
        if form_post.is_valid():
            form_post.save()
            return listadoMascotas(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)
@login_required


def eliminarMascota(request, id):
    mascota=Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('/mascotas')
@login_required

def actualizarMascota(request, id):
    mascota=Mascota.objects.get(id=id)
    form=forms.RegistroMascotaForm(instance=mascota)
    if request.method == 'POST':
        form=forms.RegistroMascotaForm(request.POST,instance=mascota)
        if form.is_valid():
            form.save()
            return listadoMascotas(request)
    data={'form':form}
    return render(request,'agregar.html',data)

#---------------------------------------------------- 
#DIRECTOR
#----------------------------------------------------

def listadoDueños(request):
    dueños=Dueño.objects.all()
    data={'dueños':dueños}
    return render(request,'listadop.html',data)
@login_required

def agregarDueño(request):
    form=forms.RegistroDueño()
    if request.method == 'POST':
        form=forms.RegistroDueño(request.POST)
        if form.is_valid():
            form.save()
            return listadoDueños(request)
    data={'form':form}
    return render(request,'agregarp.html',data)
@login_required

def eliminarDueño(request, id):
    dueño=Dueño.objects.get(id=id)
    dueño.delete()
    return redirect('/dueños')
@login_required

def actualizarDueño(request, id):
    dueño=Dueño.objects.get(id=id)
    form=forms.RegistroDueño(instance=dueño)
    if request.method == 'POST':
        form=forms.RegistroDueño(request.POST,instance=dueño)
        if form.is_valid():
            form.save()
            return listadoDueños(request)
    data={'form':form}
    return render(request,'agregarp.html',data)

#---------------------------------------------------- 
#Reserva de hora 
#----------------------------------------------------
def listar_reservas(request):
    reservas = ReservaHora.objects.filter(usuario=request.user)
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def reservar_hora(request, hora_id):
    hora = ReservaHora.objects.get(id=hora_id)
    hora.reservado = not hora.reservado
    hora.save()
    return redirect('listar_reservas')


