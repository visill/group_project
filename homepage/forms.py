from django import forms
from museums.models import City


CITIES = [(i.slug, i.name) for i in City.objects.all()]


class CityChoiceForm(forms.Form):
    choose_city = forms.ChoiceField(choices=CITIES, label='Выберите ваш город')
