from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductViewSetGeneric

router = DefaultRouter()
router.register("product-abc", ProductViewSetGeneric, basename="products")

urlpatterns = router.urls
