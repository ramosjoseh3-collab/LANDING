from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/#contacto'

    def form_valid(self, form):
        # Aquí se podría agregar el código para enviar un email si se requiere en el futuro
        messages.success(self.request, '¡Gracias por tu mensaje! Me pondré en contacto contigo a la brevedad.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrige los errores en el formulario.')
        return super().form_invalid(form)
