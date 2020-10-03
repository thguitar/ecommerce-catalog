from django.conf.urls.static import static
from django.urls import path, include

from EcommerceCatalog import settings

urlpatterns = [
  path('rest_auth/', include('rest_auth.urls')),
  path('rest_auth/registration/', include('rest_auth.registration.urls')),
  path('api/', include('api.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
