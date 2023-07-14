from rest_framework.routers import SimpleRouter

from products.viewsets import ProductModelViewSet, ProductGenericViewSet


router = SimpleRouter()
# router.register('products', ProductModelViewSet, basename="products")
router.register('products', ProductGenericViewSet, basename="products")
print(router.urls)
urlpatterns = router.urls