from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from homepage import views

app_name = "homepage"

urlpatterns = [
    path("", views.CityFormHPClass.as_view(), name="home"),
    path("<city_slug>", views.HPEventsView.as_view(), name="homepage_events"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
