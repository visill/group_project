from django.urls import path

from museums import views

urlpatterns = [
    path('museum/<slug>', views.todo, name='museum_detail'),
    path('exhibit/<slug>', views.todo, name='exhibit_detail'),
    path('museums/', views.todo, name='museum_list'),
    path('', views.todo, name='homepage'),
]
