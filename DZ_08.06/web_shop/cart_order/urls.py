from rest_framework import routers

from cart_order.views import CartViewSet, OrderViewSet


router = routers.SimpleRouter()
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
