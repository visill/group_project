from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from events.views import EventDetailView

app_name = "events"

urlpatterns = [path("<slug>", EventDetailView.as_view(), name="event_detail")]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
