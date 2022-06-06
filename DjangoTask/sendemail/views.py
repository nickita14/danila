from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ContactForm



def index(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
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
        else:
            return HttpResponse('Неверный запрос.')
    return render(request, "sendemail/index.html", {'form': form, 'title' : 'Sweets'})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')