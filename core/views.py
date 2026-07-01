from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/#contacto'

    def form_valid(self, form):
        nombre = form.cleaned_data.get('nombre')
        email = form.cleaned_data.get('email')
        telefono = form.cleaned_data.get('telefono', 'No proporcionado')
        mensaje = form.cleaned_data.get('mensaje')

        asunto = f'Nueva consulta web de {nombre}'
        cuerpo = f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\n\nMensaje:\n{mensaje}'

        try:
            send_mail(
                asunto,
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error al enviar correo: {e}")

        messages.success(self.request, '¡Gracias por tu mensaje! Me pondré en contacto contigo a la brevedad.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrige los errores en el formulario.')
        return super().form_invalid(form)
