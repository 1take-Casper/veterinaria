from django import forms
from appfutbolista.models import Mascota,Dueño,ReservaHora

class RegistroMascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

    SEXO = [
        ('f', 'F'),
        ('m','M'),
    ] 

    nombre = forms.CharField()
    edad = forms.IntegerField()
    fecha_de_nacimiento = forms.DateField()
    sexo = forms.CharField(widget=forms.Select(choices=SEXO))
    


    nombre.widget.attrs['class']='form-control'
    edad.widget.attrs['class']='form-control'
    fecha_de_nacimiento.widget.attrs['class']='form-control'
    sexo.widget.attrs['class']='form-control'


class RegistroDueño(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = '__all__'

    apellido_paterno = forms.CharField()
    apellido_materno = forms.CharField()
    nombres = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput)
    motivo_de_visita = forms.CharField()

    apellido_paterno.widget.attrs['class']='form-control'
    apellido_materno.widget.attrs['class']='form-control'
    nombres.widget.attrs['class']='form-control'
    fecha_nacimiento.widget.attrs['class']='form-control'
    motivo_de_visita.widget.attrs['class']='form-control'

class ReservaHoraForm(forms.ModelForm):
    class Meta:
        model = ReservaHora
        fields = ['hora', 'reservado']

