from django.urls import path

from exhibits.views import ExhibitsDetailView, ExhibitsListView

app_name = 'exhibits'

urlpatterns = [
    path(
        '<slug>', ExhibitsDetailView.as_view(),
        name='exhibit_detail'
    ),
    path(
        'exhibit_list/<museum_slug>', ExhibitsListView.as_view(),
        name='exhibit_list'
    ),
]
