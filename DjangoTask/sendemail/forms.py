from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    from_email = forms.EmailField(label='Почта', required=True, widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    tel_number = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Тел.номер'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'placeholder': 'Сообщение', 'rows': 3}),
                              required=True)
