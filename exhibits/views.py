from django.views.generic import DetailView, TemplateView

from exhibits.models import Exhibit


class ExhibitsDetailView(DetailView):
    model = Exhibit
    template_name = "exhibit/detail.html"
    context_object_name = "exhibit"


class ExhibitsListView(TemplateView):
    template_name = "exhibit/list.html"

    def get(self, response, *args, **kwargs):
        context = {
            "exhibits": (
                Exhibit.objects.filter(museum__slug=kwargs["museum_slug"])
            )
        }
        return self.render_to_response(context)
