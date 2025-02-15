from django import forms


class ClientRequestForm(forms.Form):

    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    telegram = forms.CharField(label='Телеграм', max_length=255)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    