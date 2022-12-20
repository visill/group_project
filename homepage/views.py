from django.http import HttpResponse
from django.views.generic import FormView
from .forms import CityChoiceForm


class CityFormHPClass(FormView):
    form_class = CityChoiceForm
    template_name = 'homepage_form.html'

    def form_valid(self, form):
        self.slug = form.cleaned_data["choose_city"]
        return super().form_valid(form)

    def get_success_url(self):
        # find your next url here
        return f'/{self.slug}'
