from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from museums.models import Museum


class MuseumDetailView(TemplateView):
    template_name = "museum/detail.html"

    def get(self, request, *args, **kwargs):
        museum = get_object_or_404(Museum, slug=kwargs["slug"])
        events = museum.events.order_by("date")
        context = {"museum": museum, "events": events}
        return self.render_to_response(context)


class MuseumListView(TemplateView):
    template_name = "museum/list.html"

    def get(self, request, *args, **kwargs):
        city_museum = {}

        for i in Museum.objects.all():
            if i.city not in list(city_museum.keys()):
                city_museum[i.city] = []
            city_museum[i.city].append(i)
        context = {"museums": city_museum}
        return self.render_to_response(context)
