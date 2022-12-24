from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from about.views import DevInfoView
from about.views import AboutView

app_name = "about"

urlpatterns = [
    path("", AboutView.as_view(), name="about"),
    path("devinfo", DevInfoView.as_view(), name="devinfo"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
