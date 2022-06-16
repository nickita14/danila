from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'sendemail/index.html'
    success_url = reverse_lazy('succes')

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['title'] = 'Sweets'
        return context


    def form_valid(self, form):
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        tel_number = form.cleaned_data['tel_number']
        text = f'{from_email}\n{tel_number}\n{message}'
        try:
            send_mail(f'{name} оставил письмо на Sweets', text,
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return HttpResponse('Ошибка в теме письма.')
        return redirect('success')

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
