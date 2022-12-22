from django.urls import path

from museums import views

app_name = "museums"

urlpatterns = [
    path("<slug>/", views.MuseumDetailView.as_view(), name="museum_detail"),
    path("", views.MuseumListView.as_view(), name="museum_list"),
]
