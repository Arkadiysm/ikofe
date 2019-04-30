from django import forms
from .mail import create_and_send_mail


class IkofeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    phone_number = forms.CharField(max_length=15, label='Телефон')


def form_handler(req, form):
    form = form(req.POST)
    if form.is_valid():
        name, number = form.name, form.phone_number
        text = '''
            Имя отправителя: {0}, \n
            Номер отправителя: {1}
        '''.format(name, number)

        create_and_send_mail('', 'Заявка', text)
        return True
    else:
        return False
