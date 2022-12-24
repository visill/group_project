from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.views.generic import TemplateView

from events.models import MuseumEvent
from homepage.forms import CityChoiceForm
from museums.models import City


class HPEventsView(TemplateView):
    template_name = "homepage/homepage_events.html"

    def get(self, request, *args, **kwargs):
        city = get_object_or_404(City, slug=kwargs["city_slug"])
        events = MuseumEvent.objects.get_event_by_city(kwargs["city_slug"])[:5]
        context = {
            "events": events,
            "city": city,
        }
        return self.render_to_response(context)


class CityFormHPClass(FormView):
    form_class = CityChoiceForm
    template_name = "homepage/homepage_form.html"

    def form_valid(self, form):
        self.slug = form.cleaned_data["choose_city"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage:homepage_events', args=[self.slug])
