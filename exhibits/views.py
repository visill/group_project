from django.urls import reverse
from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from exhibits.models import Exhibit
from about.forms import MuseumChoiceForm


class ExhibitsMainView(FormView):
    form_class = MuseumChoiceForm
    template_name = "exhibit/main.html"

    def form_valid(self, form):
        self.slug = form.cleaned_data["museum"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('exhibits:exhibit_list', args=[self.slug])


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
