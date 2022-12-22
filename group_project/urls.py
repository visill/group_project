from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homepage.urls')),
    path('exhibits/', include('exhibits.urls')),
    path('museums/', include('museums.urls')),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
