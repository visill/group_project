from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from exhibits.views import ExhibitsDetailView, ExhibitsListView

app_name = "exhibits"

urlpatterns = [
    path("<slug>", ExhibitsDetailView.as_view(), name="exhibit_detail"),
    path("exhibit_list/<museum_slug>", ExhibitsListView.as_view(), name="exhibit_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
