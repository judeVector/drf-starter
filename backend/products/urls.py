from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductMixinView,
)

urlpatterns = [
    path("<int:pk>/", ProductMixinView.as_view()),
    path("", ProductListCreateAPIView.as_view()),
]
