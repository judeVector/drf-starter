from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductCreateAPIView,
    ProductMixinView,
)

urlpatterns = [
    path("<int:pk>/", ProductMixinView.as_view()),
    path("", ProductCreateAPIView.as_view()),
]
