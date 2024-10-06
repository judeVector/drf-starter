from django.urls import path

from .views import ProductDetailAPIView, ProductCreateAPIView, ProductMixinView

urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    path("", ProductMixinView.as_view()),
]
