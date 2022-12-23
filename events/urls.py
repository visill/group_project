from django.urls import path

from events.views import EventDetailView

app_name = "events"

urlpatterns = [path("<slug>", EventDetailView.as_view(), name="event_detail")]
