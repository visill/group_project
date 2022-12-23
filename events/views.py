from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from events.models import Museum, MuseumEvent


class EventDetailView(TemplateView):
    template_name = "events/event_detail.html"

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(MuseumEvent, slug=kwargs["slug"])
        museum = Museum.objects.get(slug=event.museum.slug)
        context = {"museum": museum, "event": event}
        return self.render_to_response(context)
