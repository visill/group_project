from django.views.generic import TemplateView
from django.views.generic import FormView

from homepage.forms import CityChoiceForm
from events.models import MuseumEvent
from museums.models import City


class HPEventsView(TemplateView):
    template_name = "homepage/homepage_events.html"

    def get(self, request, *args, **kwargs):
        events = MuseumEvent.objects.filter(
            museum__city__slug=kwargs['city_slug']
        ).order_by('-date')[:5]
        city = City.objects.get(slug=kwargs['city_slug'])
        context = {
            'events': events,
            'city': city,
        }
        return self.render_to_response(context)


class CityFormHPClass(FormView):
    form_class = CityChoiceForm
    template_name = "homepage/homepage_form.html"

    def form_valid(self, form):
        self.slug = form.cleaned_data["choose_city"]
        return super().form_valid(form)

    def get_success_url(self):
        # find your next url here
        return f"/{self.slug}"
