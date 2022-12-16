from django.views.generic import DetailView

from exhibits.models import Exhibit


class ExhibitsDetailView(DetailView):
    model = Exhibit
    template_name = 'exhibit/detail.html'
    context_object_name = 'exhibit'
