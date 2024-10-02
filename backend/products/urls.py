from django.urls import path

from .views import ProductDetailAPIView, ProductCreateAPIView

urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    path("", ProductCreateAPIView.as_view()),
]
