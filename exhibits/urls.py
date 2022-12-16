from django.urls import path

from exhibits.views import ExhibitsDetailView

app_name = 'exhibits'

urlpatterns = [
    path(
        '<slug>', ExhibitsDetailView.as_view(),
        name='exhibit_detail'
    ),
]
