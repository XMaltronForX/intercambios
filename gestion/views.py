from django.shortcuts import render
from django.views.generic import ListView
from .models import ProgramaIntercambio  # Asegúrate de que el modelo `Programa` existe
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

def notificar_postulacion():
    mensaje = "Un estudiante ha realizado una nueva postulación."
    send_mail(
        subject='Nueva Postulación',
        message=mensaje,
        from_email='tu_correo@gmail.com',
        recipient_list=['eliasrgatica@gmail.com'],
        fail_silently=False,
    )
    
class ProgramasListView(ListView):
    model = ProgramaIntercambio  # Actualiza el modelo aquí
    template_name = 'programas_list.html'  # Asegúrate de que esta plantilla exista
    context_object_name = 'object_list'  # Este será el nombre usado en el template

class ProgramaCreateView(CreateView):
    model = ProgramaIntercambio
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']
    template_name = 'programa_form.html'
    success_url = reverse_lazy('programas_list')

    def form_valid(self, form):
        # Asigna el usuario que está creando el programa
        form.instance.creado_por = self.request.user
        return super().form_valid(form)


class ProgramaUpdateView(UpdateView):
    model = ProgramaIntercambio
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']
    template_name = 'programa_form.html'
    success_url = reverse_lazy('programas_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Editar'
        return context


class ProgramaDeleteView(DeleteView):
    model = ProgramaIntercambio
    template_name = 'programa_confirm_delete.html'  # Plantilla para confirmar la eliminación
    success_url = reverse_lazy('programas_list')  # Redirige a la lista de programas después de eliminar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Eliminar'
        return context
