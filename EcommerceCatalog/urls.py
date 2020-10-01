from django.urls import path, include

urlpatterns = [
  path('rest_auth/', include('rest_auth.urls')),
  path('rest_auth/registration/', include('rest_auth.registration.urls')),
  path('api/', include('api.urls'))
]
