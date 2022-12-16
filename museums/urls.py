from django.urls import path

from museums import views
app_name = 'museums'

urlpatterns = [
    path('<slug>/', views.todo, name='museum_detail'),
    path('', views.todo, name='museum_list'),
]
