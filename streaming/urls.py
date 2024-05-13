from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

import myapp.views as myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.main, name='main'),
    path('list_of_accommodations/', include('myapp.urls', namespace='acc')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
