from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from products.views import product_list_create_view

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/products/", product_list_create_view, name="product-list"),
]


# from rest_framework.authtoken.views import obtain_auth_token

# from .views import api_home

# urlpatterns = [path("auth/", obtain_auth_token), path("", api_home, name="api_home")]
