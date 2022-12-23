from django import forms

from museums.models import City

from .utils import is_migration


class CityChoiceForm(forms.Form):
    cities = []

    if not is_migration():
        cities = [(i.slug, i.name) for i in City.objects.all()]

    choose_city = forms.ChoiceField(choices=cities, label="Выберите ваш город")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control form-select"
