from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from museums import views

app_name = "museums"

urlpatterns = [
    path("<slug>/", views.MuseumDetailView.as_view(), name="museum_detail"),
    path("", views.MuseumListView.as_view(), name="museum_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
