from django import forms

from museums.models import Museum


class MuseumChoiceForm(forms.Form):
    museums = [(i.slug, i.name) for i in Museum.objects.all()]

    museum = forms.ChoiceField(
        choices=museums,
        label="Выберите музей, экспонаты которого вы хотите видеть"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control form-select"
