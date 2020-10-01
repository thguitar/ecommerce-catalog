from django.urls import path, include
from rest_framework import routers

from api import views

api_router = routers.DefaultRouter()
api_router.register("categorias", views.CategoriaViewSet)
api_router.register("produtos", views.ProdutoViewSet)

urlpatterns = [
  path('', views.Index.as_view()),
  path('v1/', include(api_router.urls))
]
