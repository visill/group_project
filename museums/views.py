from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import Museum


class MuseumDetailView(TemplateView):
    template_name = 'museum/detail.html'

    def get(self, request, *args, **kwargs):
        museum = get_object_or_404(Museum, slug=kwargs['slug'])

        context = {"museum": museum}
        return self.render_to_response(context)


class MuseumListView(TemplateView):
    template_name = 'museum/list.html'

    def get(self, request, *args, **kwargs):
        city_museum = {}

        for i in Museum.objects.all():
            if i.city not in list(city_museum.keys()):
                city_museum[i.city] = []
            city_museum[i.city].append(i)
        context = {"museums": city_museum}
        return self.render_to_response(context)
