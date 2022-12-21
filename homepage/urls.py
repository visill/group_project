from django.urls import path

from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.CityFormHPClass.as_view(), name='home'),
    path('<city_slug>', views.HPEventsView.as_view(), name='homepage_events'),
]
